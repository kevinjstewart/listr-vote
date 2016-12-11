import http.client
import time

# Initial HTTP config
conn = http.client.HTTPConnection("www.listr.top")

headers = {
    'content-type': "application/json",
    }

print("--- Listr Voting Bot ---")
print("What is the post ID that you want to manipulate? ")
post_id = input('Post ID: ')
try:
    count = int(input('How many times do you want to do this? '))
except ValueError:
    print('Not a number.')
    raise SystemExit(1)

voting_pref = input('Great. Upvote (U) or Downvote (D)? ')

# Check response
if voting_pref in ['U', 'u', 'upvote', 'Upvote', 'UPVOTE']:
    url_string = "/Questions/UpVote"
elif voting_pref in ['D', 'd', 'downvote', 'Downvote', 'DOWNVOTE']:
    url_string = "/Questions/DownVote"
else:
    print("Not an option!")
    raise SystemExit(1)

# Set post to manipulate
payload = "{\"id\":\"" + post_id + "\"}"

for i in range (0, count):
    print("Request #" + str(i))
    conn.request("POST", url_string, payload, headers)
    res = conn.getresponse()
    data = res.read()
    print("Server response: " + data.decode("utf-8"))
    time.sleep(2)

