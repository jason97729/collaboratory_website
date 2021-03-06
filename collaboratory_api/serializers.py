#serializers.py

from rest_framework import serializers
from .models import Region, Role, Cause, User, Organization, Event, Channel, Post, Organization_Region, Organization_Cause_Alignment, User_Event_Attendance, Announcement
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User as auth_user


class RegionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Region
		fields = ('region_id', 'name')

class RoleSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Role
		fields = ('role_id', 'name')

class CauseSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Cause
		fields = ('cause_id', 'name')

class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
	cause_id = serializers.SlugRelatedField(
	many=True,
	read_only=True,
	slug_field='name'
	)
	region_id = serializers.SlugRelatedField(
	many=True,
	read_only=True,
	slug_field='name'
	)
    # cause = serializers.SlugRelatedField(read_only=True, slug_field='name', many=True)
    # region = serializers.SlugRelatedField(read_only=True, slug_field='name', many=True)
	class Meta:
		model = Organization
		fields = ('org_id', 'ein', 'name', 'address1', 'address2', 'city', 'state', 'zip', 'country', 'phone', 'mission', 'website', 'facebook', 'twitter', 'founded', 'cause_id', 'region_id')

class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = auth_user
        fields = ('username', 'first_name', 'last_name', 'email')

class UserSerializer(serializers.HyperlinkedModelSerializer):
	user = AuthUserSerializer(required=True)
	organization_id = OrganizationSerializer(read_only=True)

	class Meta:
		model = User
		fields = ( 'user', 'phone', 'preferred_pronouns', 'registration_date', 'role_id', 'organization_id')

class EventSerializer(serializers.HyperlinkedModelSerializer):
	# user_id = AuthUserSerializer(required=True)

	class Meta:
		model = Event
		fields = ('name', 'date', 'location', 'RSVP', 'description', 'user')

class ChannelSerializer(serializers.HyperlinkedModelSerializer):
	# user_id = UserSerializer(read_only=True)
	class Meta:
		model = Channel
		fields = ('channel_id', 'name', 'description')

#TODO: Delete, unused
class AnnouncementSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Announcement
		fields = ('announcement_id', 'title', 'text', 'date', 'user_id', 'event_id')

class PostSerializer(serializers.HyperlinkedModelSerializer):
	# user_id = AuthUserSerializer(required=True)
	# channel_id = ChannelSerializer(read_only=True)
	# channel_id = ChannelSerializer(read_only=True)
	# user_id = UserSerializer(read_only=True)

	class Meta:
		model = Post
		fields = ('title', 'text', 'channel', 'user')

	# def createChannel(self, validated_data):
	# 	channel_data = validated_data.pop('channel_id')
	# 	post = Post.objects.create(**validated_data)
	# 	Channel.objects.create(post=post, **channel_data)
	# 	return post

	# def createUser(self, validated_data):
	# 	user_data = validated_data.pop('user_id')
	# 	post = Post.objects.create(**validated_data)
	# 	User.objects.create(post=post, **user_data)
	# 	return post

class OrganizationRegionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Organization_Region
		fields = ('id', 'organization_id', 'region_id')

#TODO: Delete, unused
class OrganizationCauseSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Organization_Cause_Alignment
		fields = ('id', 'organization_id', 'cause_id')

#TODO: Delete, unused
class UserEventSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User_Event_Attendance
		fields = ('id', 'user_id', 'event_id')
