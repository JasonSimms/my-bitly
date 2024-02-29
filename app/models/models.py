class AuthUser:
    def __init__(
        self, email: str, uid: str = None, displayName: str = None, photoUrl: str = None
    ):
        self.uid = uid
        self.email = email
        self.displayName = displayName
        self.photoUrl = photoUrl


class CampaignLink:
    def __init__(
        self,
        id: str,
        campaignId: str,
        linkId: str,
        shortUrl: str,
        createdAt: str = None,
        updatedAt: str = None,
    ):
        self.id = id
        self.campaignId = campaignId
        self.linkId = linkId
        self.shortUrl = shortUrl
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        self.clicks = []  # Initialize an empty list to store click history


class Click:
    def __init__(self, id: str, shortLinkId: str, ipAddress: str):
        self.id = id
        self.shortLinkId = shortLinkId
        self.ipAddress = ipAddress


class Campaign:
    def __init__(
        self,
        id: str,
        userId: str,
        name: str,
        campaignLinkIds: list[str],
        createdAt: str = None,
        updatedAt: str = None,
    ):
        self.id = id
        self.userId = userId
        self.name = name
        self.campaignLinkIds = campaignLinkIds
        self.createdAt = createdAt
        self.updatedAt = updatedAt


class UserLink:
    def __init__(
        self,
        id: str,
        url: str,
        nickname: str = None,
        notes: str = None,
        linkIcon: str = None,
        createdAt: str = None,
        updatedAt: str = None,
    ):
        self.id = id
        self.url = url
        self.nickname = nickname
        self.notes = notes
        self.linkIcon = linkIcon
        self.createdAt = createdAt
        self.updatedAt = updatedAt
