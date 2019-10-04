import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Sum, Max
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from cricketapp.models import Match, Inning, PlayerScoreCard, Team, Player, MatchPlayerDetails, Club
from django.utils import timezone
from cricketapp.serializers import PlayerDetailSerializer, TeamListSerializer


class DashboardView(View):

    # login_url='match/login/'

    def get(self,request):
        year = datetime.datetime.today().year
        match_list = Match.objects.filter(created_at__year = year)
        matches_list = []
        match_detail = {}
        team_list = Team.objects.all()
        for match_obj in match_list:
            match_description = match_obj.team_1.name + ' vs ' + match_obj.team_2.name
            match_date = match_obj.match_date
            if timezone.now() < match_date:
                status = "Match yet to start"
            elif match_date.date() == timezone.now().date():
                status = "Match is running "
            else:
                status = match_obj.winner
            team_1 = match_obj.team_1.id
            team_2 = match_obj.team_2.id
            context={
                "match_description":match_description,
                "match_date":match_date,
	            "status":status,
	            "team_1":team_1,
	            "team_2":team_2,
	            "id":match_obj.id,
            }
            matches_list.append(context)
        point_list = []
        for team_id in team_list:
            match_list = MatchPlayerDetails.objects.filter(team_id = team_id)
            point_count = Inning.objects.filter(match_player__in =match_list,status = "won").count()
            context = {
                "point":point_count,
                "team_name":team_id.name
            }
            point_list.append(context)
        point_list.sort(key = lambda x: x['point'],reverse = True)
        match_detail["matches_list"]= matches_list[0:5]
        match_detail["team_list"]= team_list
        match_detail["point_list"]= point_list
        return render(request, "dashboard.html",{"match_detail":match_detail})


class MatchView(View):

    def get(self,request):
        team_list = Team.objects.all()
        return render(request,"match_add.html",{"team_list":team_list})


    def post(self,request):
        data = self.request.POST
        match_date = data.get("match_date")
        match_date = datetime.strptime(match_date,'%m/%d/%Y')
        team1 = data.get("team1")
        team2 = data.get("team2")
        team_obj1 = Team.objects.get(id = int(team1))
        team_obj2 = Team.objects.get(id = int(team2))
        Match.objects.create(match_date = match_date,team_1=team_obj1,team_2 =team_obj2)
        return redirect("cricketapp:dashboard")

##Team listing Ajax
class AjaxTeamListView(View):

    def post(self, request):
        team_id = request.POST.get('id')
        team_obj = Team.objects.all().exclude(id=team_id)
        team_list = TeamListSerializer(team_obj, many=True)

        if team_list is not None:
            result = team_list.data
            status = 'success'
        else:
            result = ''
            status = 'error'

        return JsonResponse({'result': result, 'status': status})

class PlayerListView(View):

    def get(self,request,*args,**kwargs):
        team_id = self.kwargs.get('pk')
        query = request.GET.get('search')

        if query is not None:
            lookups = Q(first_name__icontains=query,team__id=team_id,is_delete=False) | Q(last_name__icontains=query,team__id=team_id,is_delete=False)
            player_list = Player.objects.filter(lookups)
        else:
            player_list = Player.objects.filter(team__id=team_id,is_delete=False)

        return render(request, "player_list.html", {"player_list": player_list,"team_id":team_id})


class AddPlayerView(View):
    def get(self,request,*args,**kwargs):
        team_id = self.kwargs.get('pk')

        return render(request, "player_add.html", {"team_id":team_id,"title":"Add Player"})

    def post(self,request,*args,**kwargs):
        team_id = self.kwargs.get('pk')
        team_obj = Team.objects.get(id=team_id)
        image = request.FILES["image"]
        data = self.request.POST
        jersy = data.get("jersy")
        # match_date = datetime.strptime(match_date, '%m/%d/%Y')
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        Player.objects.create(team = team_obj,player_jersey_number =jersy,
                              image_uri = image,first_name=first_name,last_name=last_name)
        return redirect(reverse("cricketapp:player-list",kwargs={"pk":team_id}))

class DeletePlayerView(View):
    def get(self,request,**kwargs):
        player_id = self.kwargs.get('pk')
        player_obj = Player.objects.filter(id=player_id)
        if player_obj.exists():
            player_obj.update(is_delete = True)
        return redirect(reverse("cricketapp:player-list", kwargs={"pk": player_obj[0].team.id}))




class PlayerDetailView(View):
    def get(self,request,*args,**kwargs):
        player_id = self.kwargs.get('pk')
        try:
            player_obj = Player.objects.get(id=player_id)
            name = player_obj.first_name +" "+ player_obj.last_name
        except:
            pass
        player_detail = PlayerScoreCard.objects.filter(player=player_obj)
        Match_count = 0
        Total_runs = 0
        Higest_run = 0
        Fifty = 0
        Hundred = 0
        if player_detail.exists():
            Match_count = player_detail.count()
            Total_runs = player_detail.aggregate(Sum('runs'))
            Higest_run = player_detail.aggregate(Max('runs'))
            Fifty = player_detail.aggregate(Sum('fifty'))
            Hundred = player_detail.aggregate(Sum('hundred'))

        player_detail_dict = {
            "name":name,
            "match" : Match_count,
            "run":Total_runs,
            "higest_run":Higest_run,
            "fifty":Fifty,
            "hundred":Hundred
        }
        return render(request, "player_detail.html", {"player_detail":player_detail_dict,"title":"Player Detail"})


class AddTeamView(View):

    def get(self,request,*args,**kwargs):
        club_list = Club.objects.filter(is_active = True)
        return render(request, "add_team.html", {"club_list":club_list,"title":"Add Team"})


    def post(self,request,*args,**kwargs):
        flag = request.FILES["flag"]
        data = self.request.POST
        team_name = data.get("team_name")
        club = data.get("club")
        try:
            club_obj = Club.objects.get(id = int(club))
        except:
            pass
        Team.objects.create(club = club_obj,name = team_name,logo = flag)
        return redirect("cricketapp:dashboard")


class MatchScoreView(View):
    def get(self,request,*args,**kwargs):
        match_id = request.GET.get('match_id')
        team_1 = request.GET.get('team_1')
        team_2 = request.GET.get('team_2')
        match_detail = MatchPlayerDetails.objects.filter(match_id__id = int(match_id),team_id__id = int(team_1))
        player_score_1 = []

        if match_detail.exists():
            try:
                inning_1 = Inning.objects.filter(match_player__in =match_detail)
                player_score_1 = PlayerScoreCard.objects.filter(inning__in =inning_1 )
            except:
                pass

        match_detail = MatchPlayerDetails.objects.filter(match_id__id=int(match_id), team_id__id=int(team_2))
        player_score_2 = []
        if match_detail.exists():
            try:
                inning_2 = Inning.objects.filter(match_player__in=match_detail)
                player_score_2 = PlayerScoreCard.objects.filter(inning__in=inning_2)
            except:
                pass
        return render(request, "score.html", {"match_id":match_id,"team_1":team_1,"team_2":team_2,"player_score_2": player_score_2,"player_score_1":player_score_1, "title": "Match Score"})

class AddScoreView(View):

    def get(self,request,*args,**kwargs):
        match_id = request.GET.get('match_id')
        team = request.GET.get('team')
        match_detail = MatchPlayerDetails.objects.filter(match_id__id=int(match_id), team_id__id=int(team))

        return render(request, "add_score.html",
                      {"match_detail": match_detail,"title": "Add Score"})

    def post(self,request):
        match_id = request.GET.get('match_id')
        team = request.GET.get('team')
        match_detail = MatchPlayerDetails.objects.filter(match_id__id=int(match_id), team_id__id=int(team))
        inning_obj, created = Inning.objects.get_or_create(match_player__in=match_detail)
        data = self.request.POST
        id_list = data.getlist("id")
        for id in id_list:
            player_id = data.get("name_{}".format(id))
            runs = data.get("run_{}".format(id),None)
            fours = data.get("fours_{}".format(id),None)
            sixes = data.get("sixes_{}".format(id),None)
            status = data.get("status_{}".format(id),None)
            try:
                player_obj = Player.objects.get(id=player_id)
                player_score_obj,created = PlayerScoreCard.objects.get_or_create(inning=inning_obj,player=player_obj)
                player_score_obj.runs =runs
                player_score_obj.fours =fours
                player_score_obj.sixes =sixes
                player_score_obj.status =status
                player_score_obj.save()
            except:
                pass

        return redirect("cricketapp:dashboard")