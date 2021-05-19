#!/usr/bin/env bash
# Author: kNIGHT

TOKEN="1851626686:AAFxreKorxHjDV_l7o9ryswEMGBfsi40Yxs"
CHATID="-1001208308421"
PHOTO="banner.jpg"
device=$1
legv=$2
codename=$3
patch_date=$4
username=$5
	curl -X POST -F photo=@"${PHOTO}" https://api.telegram.org/bot"${TOKEN}"/sendPhoto -F chat_id="${CHATID}" -F parse_mode=Markdown -F "caption=*LegionOS ${legv}* | *${device}* | ${codename} 
	
	▪️ *Build date* : $(date +%Y-%m-%d)
	▪️ *Security Patch* : ${patch_date}
	▪️ *Android Version* : 11
	▪️ *Download* : [HERE](https://legionos.org)
	(Builds may take upto 30mins to show up.... until then it will show error in OTA and site...please bare with us)

	▪️ *By* : @${username}
	▪️ *Support* : [ROM](https://t.me/legionos)
	
	#LegionOS #${device} #${codename}"
