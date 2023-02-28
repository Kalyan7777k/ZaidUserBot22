import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "24164661")) #optional
API_HASH = getenv("API_HASH", "4509cb7792bdfb55744a89183a6083ae") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5890959459 5134001652").split()))
OWNER_ID = int(getenv("OWNER_ID"  "5134001652"))
MONGO_URL = getenv("MONGO_URL"  "mongodb+srv://babukalyan977:babukalyan977@cluster0.fvkyo4r.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "6113040968:AAHgbh90qCMxxxx6yiKA_3mfRBifSH7RPOg")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://telegra.ph/file/3c52a01057865f7511168.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER"  "welcome to pm 🌹")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBzxok1qJm50ARo9trp2kqMxym08b0dTD_bW2PLwR4819TWseEFxHYvEtLoARedysg-s2vJcluvXvGvL3f1AXQ0_qJbYPqBCXwkHTU0nlMKSor7Hz49WGE5vTsRjgs-NO1vvAMZ7Nz1PXItS_DShg8Thd6-JBPStnsBAGE_DgtNtbHZa8rFtc1obLmhAN_PuC1lJgFnxb8i4_YVnUE94C2xDvV8q4NjL3-_meoszZWECPYqqQJpr9VYD96KaETF-YPIrW9ggUm29VihdJ8aSMpwhHiRs3AAt3yfDoNrnvGGpU69gDA05XjmmvOs7kUvdT0daJ76l_hUqC31EPUv3j0wAAAAAUKzuAMA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
