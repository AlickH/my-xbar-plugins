#!/opt/homebrew/bin/python3

# <xbar.title>Focus</xbar.title>
# <xbar.version>v1</xbar.version>
# <xbar.author>A.Lick</xbar.author>

import urllib3
import json
import sys,os

surgeLight = "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAhGVYSWZNTQAqAAAACAAFARIAAwAAAAEAAQAAARoABQAAAAEAAABKARsABQAAAAEAAABSASgAAwAAAAEAAgAAh2kABAAAAAEAAABaAAAAAAAAAJAAAAABAAAAkAAAAAEAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAIKADAAQAAAABAAAAIAAAAAC+voNmAAAACXBIWXMAABYlAAAWJQFJUiTwAAABWWlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iWE1QIENvcmUgNi4wLjAiPgogICA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPgogICAgICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIgogICAgICAgICAgICB4bWxuczp0aWZmPSJodHRwOi8vbnMuYWRvYmUuY29tL3RpZmYvMS4wLyI+CiAgICAgICAgIDx0aWZmOk9yaWVudGF0aW9uPjE8L3RpZmY6T3JpZW50YXRpb24+CiAgICAgIDwvcmRmOkRlc2NyaXB0aW9uPgogICA8L3JkZjpSREY+CjwveDp4bXBtZXRhPgoZXuEHAAADFklEQVRYCa2XvYuUMRDG9zw9VA5RC8GvQu4OQbASWxvB3n/gChutLC0tBdG/x0ZYFBRLC1EbwUX8QERU/Dz11OeXzfNe9r34bvLuDTzJJDOZmcwkeXcHg/40p6U7hO0CPDQ/7gaX1K8LI+G0AKG3ZYRDO8XoNsEOjohfE/5G3FdvQm+CNk1MSPMDHNs4uzsu/Ilz6gb7BIJhDloUHGzamw9KpQ2LHPQN8QSCowuC6YSY34KDemiBekrk9Uy7ZPBFRM0h0vxTcCaeincJToqn/rkA7JwsBVue0LiKdkn7l8BOIQJZCFx3Q1BXhDfCI+GUUEXOwJJWfROcgSfiCQrKZcAbXZHca+iHFrCwhjgLACM1tD8qkz1osW8A4+UbbemJdsl8+Na3KoCNUOq4uZIAnO4603lt75zDCE0NgAB9aEqCDVY7mi9R5iu7Ns0okR4Q9grwpbWW6gR5x9yW61HyTv3VCa1k4FRd1NwP4aNwPpEvi/8uYJgM8RB1XUOJA3kDxzTiMcqSne+R9LPgEjwT78embwDYTrM+nw4kC+QoCQDnPKsQdfMuw8R/Gtak5WKcEjJs4TtcQxyyM2DnYhvHzogNI+siG6d0EOPULnO8BwQShBjmw2KyMr15ZO2x9d17p281wTPNZxh6LSBjvXXEjsklOKfh2TjnlMdhcRd2JG0+NKvCY2EoXBYgMmmdMOHmphgiA9c8qf6QkB7CkcacC2hZaN8Cf6hcsqAYG280nWt4O6d/L9jJYfF9A6DuplxAljVXwh8JvlLp4kaxgmEj2GPX4aR3rbUzpyh7ULoMdMiy9W7r4xhFn/aiRW0js4ydJt9ZDlKajVLbpL0X4eyF4BfulfgP0dK0bODUmZspAD4yd4U7wqowzbFUmp/X/mmVZg75TLQQV+feAb9uXFUeHHYObgsml9DjqX16T+F9Mw6K/yTYyXPxOwXTGTEPhFvCUpxMbcWpso5aup4O4Kjmvgr+n/dS/G4Byjmq3vnY1ObWhqjrSHAG7rVUCRRdgskF1FKvG9og/1yGAmleiSYcIENnLYrqu39VPrFpu7DKbAAAAABJRU5ErkJggg=="

surgeDark="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"

head = {
  "Content-Type": "application/json",
  "X-Key": "examplekey"
}

def surgeAPI(path):
  http = urllib3.PoolManager()
  out = http.request(
    "GET",
    "http://127.0.0.1:6166/v1/" + path,
    headers = head)
  out = json.loads(out.data)
  return(out)

def surgeMode(sub):
  mode = surgeAPI("outbound")['mode']
  outbounds = {"direct":"直接连接", "proxy":"全局代理", "rule":"规则模式"}
  status = outbounds[mode]
  for key in outbounds:
    outbound = outbounds[key]
    outboundmenu = "| trim=false | shell='./modules/toggle.sh' | param1=\"mode\" | param2=\"" + key + "\"| param3=\"outbound\""
    if outbound == status:
      print(sub + "♥  " + outbound + outboundmenu)
    else:
      print(sub + "♡  " + outbound + outboundmenu)

def surgeModules(sub):
  modules = surgeAPI("modules")
  available = modules['available']
  enabled = modules['enabled']
  for i in available:
    if i in enabled:
      print(sub + "♥  " + i + "| trim=false | shell='./modules/toggle.sh' | param1=\"" + i + "\" | param2=\"false\"| param3=\"modules\"")
    else:
      print(sub + "♡  " + i + "| trim=false | shell='./modules/toggle.sh' | param1=\"" + i + "\" | param2=\"true\"| param3=\"modules\"")

def surgePolicy(sub):
  mode = surgeAPI("outbound")['mode']
  policies = surgeAPI("policies")
  policygroups = surgeAPI("policy_groups")
  proxy = policies["proxies"]
  keys = policies["policy-groups"]
  proxy.extend(keys)
  if mode == "rule":
    for key in keys:
      groups = policygroups[key]
      selected = surgeAPI("policy_groups/select?group_name=" + key)["policy"]
      grouptype = surgeAPI("policies/detail?policy_name=" + key)[key].split(" ")[2].split(",")[0]
      print("     ◎  " + key + "| trim=false")
      a = []
      for i in range(len(groups)):
        name = groups[i]["name"]
        selectmenu = "| trim=false | shell='./modules/select.sh' | param1=\"" + key + "\" | param2=\"" + name + "\""
        if name == selected:
          if grouptype == "select":
            a = sub + "♥  " + name + selectmenu
          else:
            a = sub + "♥  " + name
        else:
          if grouptype == "select":
            a = sub + "♡  " + name + selectmenu
          else:
            a = sub + "♡  " + name
        print(a)
  elif mode == "proxy":
    globe = surgeAPI("outbound/global")["policy"]
    for i in proxy:
      if i == globe:
        print("     ♥  " + i + "| trim=false | href=\"selected\"")
      else:
        print("     ♡  " + i + "| trim=false | shell='./modules/toggle.sh' | param1=\"policy\" | param2=\"" + i + "\"| param3=\"outbound/global\"")
  elif mode == "direct":
    print("     ♥  DIRECT | trim=false | href=\"direct\"")

darkmode = os.system("${XBARDarkMode}")
if darkmode:
  surgeicon = " | image=" + surgeLight
else:
  surgeicon = " | image=" + surgeDark

print("| font=\"icomoon\" | size=14")
print("---")
print("➤  出站模式 | color=red")
surgeMode("     ")
print("---")
print("❖  模块 | color=red")
surgeModules("     ")
print("---")
print("◉  策略组 | color=red")
surgePolicy("--")