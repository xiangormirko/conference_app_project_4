#!/usr/bin/env python

import httplib
import endpoints
from protorpc import messages
from google.appengine.ext import ndb


class ConflictException(endpoints.ServiceException):
    """ConflictException -- exception mapped to HTTP 409 response"""
    http_status = httplib.CONFLICT


class Profile(ndb.Model):
    """Profile -- User profile object"""
    displayName = ndb.StringProperty()
    mainEmail = ndb.StringProperty()
    teeShirtSize = ndb.StringProperty(default='NOT_SPECIFIED')
    conferenceKeysToAttend = ndb.StringProperty(repeated=True)


class ProfileMiniForm(messages.Message):
    """ProfileMiniForm -- update Profile form message"""
    displayName = messages.StringField(1)
    teeShirtSize = messages.EnumField('TeeShirtSize', 2)


class ProfileForm(messages.Message):
    """ProfileForm -- Profile outbound form message"""
    displayName = messages.StringField(1)
    mainEmail = messages.StringField(2)
    teeShirtSize = messages.EnumField('TeeShirtSize', 3)
    conferenceKeysToAttend = messages.StringField(4, repeated=True)


class StringMessage(messages.Message):
    """StringMessage-- outbound (single) string message"""
    data = messages.StringField(1, required=True)


class BooleanMessage(messages.Message):
    """BooleanMessage-- outbound Boolean value message"""
    data = messages.BooleanField(1)


class Conference(ndb.Model):
    """Conference -- Conference object"""
    name            = ndb.StringProperty(required=True)
    description     = ndb.StringProperty()
    organizerUserId = ndb.StringProperty()
    topics          = ndb.StringProperty(repeated=True)
    city            = ndb.StringProperty()
    startDate       = ndb.DateProperty()
    month           = ndb.IntegerProperty()
    endDate         = ndb.DateProperty()
    maxAttendees    = ndb.IntegerProperty()
    seatsAvailable  = ndb.IntegerProperty()


class ConferenceForm(messages.Message):
    """ConferenceForm -- Conference outbound form message"""
    name            = messages.StringField(1)
    description     = messages.StringField(2)
    organizerUserId = messages.StringField(3)
    topics          = messages.StringField(4, repeated=True)
    city            = messages.StringField(5)
    startDate       = messages.StringField(6)  # DateTimeField()
    month           = messages.IntegerField(7)
    maxAttendees    = messages.IntegerField(8)
    seatsAvailable  = messages.IntegerField(9)
    endDate         = messages.StringField(10)  # DateTimeField()
    websafeKey      = messages.StringField(11)
    organizerDisplayName = messages.StringField(12)


class Session(ndb.Model):
    name            = ndb.StringProperty(required=True)
    highlights      = ndb.StringProperty()
    speaker         = ndb.StringProperty(repeated=True)
    duration        = ndb.StringProperty()
    typeOfSession   = ndb.StringProperty(repeated=True)
    date            = ndb.DateProperty()
    startTime       = ndb.TimeProperty()


class SessionForm(messages.Message):
    """SessionForm -- Session outbound form message"""
    name            = messages.StringField(1, required=True)
    highlights      = messages.StringField(2)
    speaker         = messages.StringField(3, repeated=True)
    duration        = messages.StringField(4)
    typeOfSession   = messages.StringField(5, repeated=True)
    date            = messages.StringField(6)  # DateTimeField()
    startTime       = messages.StringField(7)  # TimeProperty()
    websafeConferenceKey = messages.StringField(8)
    websafeKey = messages.StringField(9)


class Wishlist(ndb.Model):
    ownerId         = ndb.StringProperty()
    sessionsInList  = ndb.StringProperty(repeated=True)
    public          = ndb.BooleanProperty()


class WishlistForm(messages.Message):
    ownerId         = messages.StringField(1)
    sessionsInList  = messages.StringField(2, repeated=True)
    public          = messages.BooleanField(3)


class SessionForms(messages.Message):
    """SessionForms -- multiple Sessions outbound form message"""
    items = messages.MessageField(SessionForm, 1, repeated=True)


class ConferenceForms(messages.Message):
    """ConferenceForms -- multiple Conference outbound form message"""
    items = messages.MessageField(ConferenceForm, 1, repeated=True)


class TeeShirtSize(messages.Enum):
    """TeeShirtSize -- t-shirt size enumeration value"""
    NOT_SPECIFIED = 1
    XS_M = 2
    XS_W = 3
    S_M = 4
    S_W = 5
    M_M = 6
    M_W = 7
    L_M = 8
    L_W = 9
    XL_M = 10
    XL_W = 11
    XXL_M = 12
    XXL_W = 13
    XXXL_M = 14
    XXXL_W = 15

class Speaker(ndb.Model):
    name            = ndb.StringProperty(required=True)
    intro           = ndb.StringProperty()
    mainEmail       = ndb.StringProperty(required=True)
    sessionKeysToAttend = ndb.StringProperty(repeated=True)

class SpeakerForm(messages.Message):
    name            = messages.StringField(1, required=True)
    mainEmail       = messages.StringField(2, required=True)
    intro           = messages.StringField(3)
    sessionKeysToAttend = messages.StringField(4, repeated=True)
    websafeKey      = messages.StringField(5)

class SpeakerForms(messages.Message):
    items = messages.MessageField(SpeakerForm, 1, repeated = True)


class ConferenceQueryForm(messages.Message):
    """ConferenceQueryForm -- Conference query inbound form message"""
    field = messages.StringField(1)
    operator = messages.StringField(2)
    value = messages.StringField(3)


class ConferenceQueryForms(messages.Message):
    """ConferenceQueryForms"""
    """multiple ConferenceQueryForm inbound form message"""
    filters = messages.MessageField(ConferenceQueryForm, 1, repeated=True)
