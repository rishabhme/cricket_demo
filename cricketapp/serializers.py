from rest_framework import serializers
from cricketapp.models import Team


class PlayerDetailSerializer(serializers.Serializer):
	player_name = serializers.SerializerMethodField()
	wicket = serializers.IntegerField()
	runs = serializers.IntegerField()
	fifty = serializers.IntegerField()
	hundred = serializers.IntegerField()
	fours = serializers.IntegerField()
	sixes = serializers.IntegerField()


	def get_player_name(self,obj):
		return "{} {}".format(obj.first_name,obj.last_name)

class TeamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id','name')