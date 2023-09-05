from SigmaMusic.core.bot import VirOP
from SigmaMusic.core.dir import dirr
from SigmaMusic.core.git import git
from SigmaMusic.core.userbot import Userbot
from SigmaMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = VirOP()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
