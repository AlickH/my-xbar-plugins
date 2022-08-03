#!/usr/bin/env python3

# <xbar.title>Countdown</xbar.title>
# <xbar.version>v2.0</xbar.version>
# <xbar.author>Pere Albujer</xbar.author>
# <xbar.author.github>P4R</xbar.author.github>
# <xbar.desc>Shows countdown of established date.</xbar.desc>
# <xbar.image>https://cloud.githubusercontent.com/assets/7404532/12356787/ae62636c-bba4-11e5-8ff8-6a1eaffcbfc2.png</xbar.image>
# <xbar.dependencies>python</xbar.dependencies>


from datetime import datetime
import sys


def dateDiffInSeconds(date1, date2):
    timedelta = date2 - date1
    return timedelta.days * 24 * 3600 + timedelta.seconds


def daysHoursMinutesSecondsFromSeconds(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    return (days)


def main():
    now = datetime.now()
    date_format = '%d-%m-%Y'
    yj = ""
    zj = "造价考试还剩："
    yjt = "19-11-2022"
    zjt = "12-11-2022"
    
    time = datetime.strptime(yjt, date_format)
    print(yj + " %d d | trim=false | size=14 | font=\"FontAwesome\"" % daysHoursMinutesSecondsFromSeconds(dateDiffInSeconds(now, time)))


if __name__ == "__main__":
    main()
