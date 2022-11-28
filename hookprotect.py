#Protected under GNU 2.0 Public license.
#Made by EpikShiba, https://github.com/EpikShiba/HookProtect/
import requests
import base64
import time
webhook2 = input("Input webhook to obfuscate: ")
if "api/webhooks" not in webhook2:
  print("Invalid Webhook!")
else:
  print("-Encrypting code")
  sample_string = webhook2
  sample_string_bytes = sample_string.encode("ascii")
  base64_bytes = base64.b64encode(sample_string_bytes)
  encodedhook = base64_bytes.decode("ascii")
  time.sleep(1)
  enkode = encodedhook.split("F")
  print("-Removing symbols")
  time.sleep(2)
  hi = "a".join(enkode)
  print("-Encoding the encrypted code")
  time.sleep(3)
  print("-Generating Encrpyted code")
  print("-----------------")
  print("Encrypted webhook: ")
  print(hi)
  time.sleep(0.5)
  print("-Your encrypted vebhook variable is: encodedhook")
  time.sleep(0.2)
  print("-Webhook successfully encrypted, please look at the embed sent to discord to finish the steps.")
  data = {
    "username" : "HookProtect"
  }
  data["embeds"] = [
      {
          "description" : f"""Thank you for using HookProtect, this is your encrypted webhook incase you forget ```{hi}```

to make this work in your program, please input the following code after your webhook to decrypt it
```py
import base64
base64_string = #Your webhook variable
base64_bytes = base64_string.encode("ascii")
sample_string_bytes = base64.b64decode(base64_bytes)
decodedhook = sample_string_bytes.decode("ascii")
```
I know this is a bit inconvinient, but in the future, the coe will inject itself into the .py file.
          """,
        "title" : "Webhook successfully protected! "
    }
]
  input("Thank you for using this tool. You can now close this window")
requests.post(webhook2, json=data)

