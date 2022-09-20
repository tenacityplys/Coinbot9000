#initialize
import random
import requests 
import datetime
import sys
import json
tumblr_key = xyzzy 
pastebin_key = xyzzy
pastebin_user_key = xyzzy 
Block_number = 0
transaction_number = 00000
Transactions = []
Transacted = []
Balances = []
Users = []
most_recent = 0
last_timestamp = 0
coinbot_id = 0

#class for transactions
class Transaction:
	def __init__(self, transaction, uuid1, uuid2, amount):
        global transaction_number
		self.transaction = transaction_number
		self.uuid1 = uuid1
		self.uuid2 = uuid2
		self.amount = amount

#define object class for user profiles
class User:
	def __init__(self, uuid, blog_url, balance): 
		uuid = tumblelog_uuid
		blog_url = url
		balance = 0

#define object class for blocks
class Block:
	def __init__(self, block_number, transaction_list, updated_balances, timestamp, hash, exchange rate, message):
		self.block_number = block_number
		transaction_list = transaction_list
		updated_balances = updated_balances
		timestamp = timestamp
		hash = hash
		exchange = exchange
		message: "Have a BlogCoin day!"

#retrieve block 1 info from post
def get_block_one():
	URL = "api.tumblr.com/v2/blog/coinbot9000.tumblr.com/posts/?api_key={key}&tag=blockchain"
	parameters = {}
	r = requests.get(url = URL, params = parameters)
	data = r.json()
	Masterpost_id = data["response"]["posts"][0]['id']
	URL = "api.tumblr.com/v2/blog/coinbot9000.tumblr.com/posts/"
	URL = (URL + Masterpost_id)
	parameters = {}
	r = requests.get(url = URL, params = parameters) 
	data = r.json()
	Masterpost_id = data["response"]["posts"[0]['post_id'] 
	global coinbot_id = data["response"]["posts"][0][tumblelog_uuid]
	first_reblog(Masterpost_id)

#getting transactions
def find_transactions():
	URL = "https://api.tumblr.com/v2/tagged?tag=BlogCoin_transaction"
	parameters = []
	r = requests.get(url = URL, params = parameters)
	data = r.json()	
	for I in data["response"]["posts"]:
		if data["response"]["posts"][i][id][timestamp] <= last_timestamp:
			continue
		transaction_post = data["response"]["posts"][I][id]
		transaction_url = data["response"]["posts"][I][blog_name]
		URL = api.tumblr.com/v2/blog/
		URL = (URL + transaction_url + "/posts/" + transaction_post)
		parameters = {}
		r = requests.get(url = URL, params = parameters)
		data2 = r.json()
		transaction_text = data2["response"]["posts"][I][content]
		transaction_uuid = data2["response"]["posts"][I][tumblelog_uuid]
		parse_transaction()
		if parse = fail:
			return
		process_transaction()

#transactions should be phrased as "[user1] [X] [user2]"
def parse_transaction():
	transaction_text_list = transaction_text.split(" ", 3)
	if transaction_uuid in Users:
		if transaction_uuid.blog_url != transaction_url:
			transaction_uuid.blog_url = transaction_url
	else:
		parse = fail
		return
	if transaction_text_list[0] != transaction_url:
		parse = fail
		fail_message = "You're trying to transfer BlogCoin from a url other than your own. Don't make me tap the 'not your keys, not your crypto' sign."
		return
	else:
		uuid1 = transaction_uuid
	for i in transaction_text_list[1]:
		period = false
		if string[I].isdigit() = true:
			continue
		elif string[I] = ".":
			if period = true:
				parse = fail
				break
			if period = false:
				period = true
				continue
		else:
			parse = fail
			break
	transaction_text_list[1] = float(transaction_text_list[1])
	if transaction_uuid.balance < transaction_text_list[1]:
		parse = fail
		return
	else:
		amount = transaction_text_list[1]
	found = false
	found_list = {}
	for i in Users:
		if i.blog_url = transaction_text_list[2]:
			if: found = false:
				uuid2 = i.uuid
				found = true
				found_list.append(uuid2)
			else:
				found_list.append(i.uuid)
	if len(found_list) > 1:	
		URL = "api.tumblr.com/v2/blog/"
		api_key = api_key
		URL = (URL + transaction_text_list[2] + ".tumblr.com/posts/text?api_key={" + api_key + "}"))
		parameters = {}
		r = requests.get(url = URL, params = parameters)
		data3 = r.json()
		if response = 404:
			parse = fail
			return
		temp_post_id = data3["response"]["posts"][0][id]
		URL = "api.tumblr.com/v2/blog/"
		URL = (URL + transaction_text_list[2] + ".tumblr.com/posts/" + temp_post_id)
		parameters = {}
		r = requests.get(url = URL, params = parameters)		
		data4 = r.json()
		user2 = data4["response"]["posts"][tumblelog_uuid]
		if tumblelog_uuid not in Users:
			Users.append(tumblelog_uuid, transaction_text_list[2], 0)	
		found_list.remove(uuid2)
		for i in found_list:	
			URL = "api.tumblr.com/v2/blog/"
			api_key = api_key
			URL = (URL + i + "/info?api_key={" + api_key + "}"))
			parameters = {}
			r = requests.get(url = URL, params = parameters)
			data3 = r.json()
			if response = 404:
				parse = fail
				continue
			temp_url = data3["response"]["blog"]["url"]
			temp_url = temp_url.split("/")
			temp_url = temp_url[2]
			temp_url = temp_url.split(".")
			temp_url = temp_url[0]
			i.blog_url = temp_url
	if found = false:
		URL = "api.tumblr.com/v2/blog/"
		api_key = api_key
		URL = (URL + transaction_text_list[2] + ".tumblr.com/posts/text?api_key={" + api_key + "}"))
		parameters = {}
		r = requests.get(url = URL, params = parameters)
		data3 = r.json()
		if response = 404:
			parse = fail
			return
		temp_post_id = data3["response"]["posts"][0][id]
		URL = "api.tumblr.com/v2/blog/"
		URL = (URL + transaction_text_list[2] + ".tumblr.com/posts/" + temp_post_id)
		parameters = {}
		r = requests.get(url = URL, params = parameters)		
		data4 = r.json()
		user2 = data4["response"]["posts"][tumblelog_uuid]
		Users.append(uuid2, transaction_text_list[2], 0)

def process_transaction(uuid1, uuid2, amount):
	transaction_number = Transaction(transaction_number, uuid1, uuid2, amount)
	Transactions.append(transaction_number)
	uuid1.balance = uuid1.balance - amount
	uuid2.balance = uuid2.balance + amount
	transaction_number = transaction_number + 1
	if uuid1 not in Transacted:
		Transacted.append(uuid1)
	if uuid2 not in Transacted:
		Transacted.append(uuid2)

#define function to find first reblog of a given reblog, with most_recent as a prerequisite variable. (Each new block's post id will be designated as most_recent once it's made.) From there, can grab first_reblog[added_text] for the hash, etc.
def first_reblog(post_id):
	URL = "api.tumblr.com/v2/blog/coinbot9000/notifications"
	parameters = {'types':'reblog_with_content'}
	r = requests.get(url = URL, params = parameters)
	data = r.json()
	smol_timestamp = 1660509760000
	for i in data["response"]["notifications"]:
		if data["response"]["notifications"][I]['target_post_id'] == post_id:
			if data["response"]["notifications"][i][timestamp] == smol_timestamp:
				number == random.randint(0,1)
				if number == 0:
					smol_timestamp = data["response"]["notifications"][i][timestamp]
				else:
					continue
			elif data["response"]["notifications"][i]['timestamp'] < smol_timestamp:
				smol_timestamp = data["response"]["notifications"][i][timestamp]
				mined_block = data["response"]["notifications"][I][post_id]
				blog_url = data["response"]["notifications"][I][from_tumblelog_name]
				mine_content = data["response"]["notifications"][I][added_text]
			else: 
				continue
		else:
			continue
	if smol_timestamp == 1660509760000:
		mined_block = None
		break
	else:
		find_block(mined_block, blog_url, mine_content)

#define function to find existing coinbot block from mined block
def find_block(post_id, url, content):
	URL = "api.tumblr.com/v2/blog/"
	URL = (URL + url + "/notes?id=" + post_id + "&mode=reblogs_with_tags")
	parameters = {}
	r = requests.get(url = URL, params = parameters) 
	data = r.json()	
	next_block = 0
	post_ids = []
	for i in data["response"][notes]:
		if data["response"][notes][i][blog_uuid] == global coinbot_id:
			if "valid block" in data["response"][notes][i]['tags']:
				if next_block != 0:
					post_ids.append(data["response"][notes][i])
				else:
					next_block = data["response"][notes][I][post_id]
					post_ids.append(next_block)
			else:
				continue
		else:
			continue
	if len(post_ids) > 1:
		api_endpoint = api.tumblr.com/v2/blog/coinbot9000.tumblr.com/posts
		api_key = key
		data = {'content':{{"type":"text", "text":"A fork has occurred. Please help. Coinbot is scared."}},
			'tags':['help, Dave, my mind is going, I can feel it']
			}
		r = requests.post(url = api_endpoint, data = data)
		response = r.text
		sys.exit(0)
	elif next_block = 0:
		reblog(post_id, content)
	else:
		first_reblog(next_block)

#define hash function
def hash(mine_content):
	hash_content = (mine_content + timestamp_text)
	hash_content = hash(hash_content)

#block mining rewards
def get_reward():
	If block_number > 1000:
		MineReward = 0
	Elif block_number > 500:
		MineReward = .1
	Elif block_number > 200: 
		MineReward = .5
	Else: 
		MineReward = 1

#define function to compute exchange rate:
def compute_exchange():
	exchange = random.randrange(1000000000, 10000000000, 3)

#create balance list:
def balance_list():
	for i in Transacted:
		str_balance = str(i.balance)
		trans = str(i.blog_url, ": ", str.balance, " BlC. ")
		Balances.append(trans)
	balances_string = ""
	for i in Balances:
		balances_string = balances_string + i

#transaction text
def text_transactions():
	Transactions_text = {}
	for i in Transactions:
		transaction_txt = str(uuid1.blog_url + " sends " + amount + "to " uuid2.blog_url + ". ")
		transactions_text.append(transaction_txt)

#generate post
def generate_block_content():
	get_reward()
	if parent_tumblelog_uuid not in Users:
		parent_tumblelog_uuid = User(self, parent_tumblelog_uuid, blog_url, 0)
		Users.append(parent_tumblelog_uuid)
	if parent_tumblelog_uuid not in Transacted:
		Transacted.append(parent_tumblelog_uuid)
	transactions.append(Transaction(transaction_number, coinbot_id, parent_tumblelog_uuid, MineReward))
	Coinbot.balance = Coinbot.balance - transaction_number.amount
	parent_tumblelog_uuid.balance = parent_tumblelog_uuid.balance + transaction_number.amount
	transaction_number = transaction_number + 1
	number_text = "Block number: " + str(block_number))
	text_transactions()
	transaction_text = Transactions_text
	balances_text = balance_list()
	timestamp_text = datetime.datetime.(now)
	hash_text = hash(content + timestamp_text)
	exchange_text = compute_exchange()
	message_text = "Have a BlogCoin day!"
	blocks.append(Block(block_number, transaction_list, updated_balances, timestamp, hash, exchange rate, message))
	post_content = [{"type": "text", "text": number_text}, {"type": "text", "text": transaction_text}, {"type": "text", "text": balances_text}, {"type": "text", "text": timestamp_text}, {"type": "text", "text": hash_text}, {"type": "text", "text": exchange_text}, {"type": "text", "text": message_text}]
    return post_content

#define function to reblog & add new block
def reblog(post_id, content):
	URL = api.tumblr.com/v2/blog/
	URL = (URL + blog_url + "/posts/" + post_id)
	r = requests.get(url = URL, params = parameters)
	data = r.json()
	reblog_key = data["response"]["posts"][0]['reblog_key']
	parent_tumblelog_uuid = data["response"]["posts"][0][parent_tumblelog_uuid]
	post_content = generate_block_content(parent_tumblelog_uuid, content)
	api_endpoint = api.tumblr.com/v2/blog/
	api_endpoint = (api_endpoint + blog_url + "/post/reblog")
	data = {'content':post_content]
		'parent_tumblelog_uuid':parent_tumblelog_uuid
		'parent_post_id':post_id
		'reblog_key':reblog_key
		'hide_trail':false
		'tags':valid_block}
	r = requests.post(url = api_endpoint, data = data)
	new_requests = r.text
	#ERROR HANDLING
	if new_requests['results'][meta][status] = 201:
		new_requests['results'][response][id] = most_recent
	elif new_requests['results'][meta][status] = 400 and new_requests['results'][errors][code] == 8002:
		#add blog_url to a list of failed reblogs
		#find the earliest reblog that works and reblog that
		#post a comment to the first reblog saying there was an error?
	elif new_requests['results'][meta][status] = 404:
		#note to user in next block re: post id and blog itself
	elif new_requests['results'][meta][status] = 500 or new_requests['results'][meta][status] == 503:
		#wait an hour and try again?
	elif new_requests['results'][meta][status] = 403 and new_requests['results'][errors][code] == 8023:
		#wait 24 hours and try again. Maybe post saying Coinbot needs to sleep, or something.
	elif new_requests['results'][meta][status] = 401:
		#something with the API key?
	else: 
		#write it to a pastebin and pause. It'll send me a notification and I'll look at it.
	#WRITE TO PASTEBIN AS BACKUP
	after_reblog(timestamp_text)

def after_reblog(timestamp_text):
	global Transactions = []
	global Transacted = []
	global Balances = []
	last_timestamp = int(timestamp_text)
	block_number = block_number + 1

#pasting block info after reblogging
def paste_block():
	block_paste_content = content + other info
	api_endpoint = https://pastebin.com/api/api_post.php
	pastebin_key = api key
	Coinbot_user_key = pastebin_user_key
	paste_name = ("Block " + block_number + " - " + datetime.datetime.now())
	data = {api_dev_key:pastebin_key
		api_option:paste
		api_paste_code:block_paste_content
		api_user_key:Coinbot_user_key
		api_paste_name:paste_name
		api_paste_format:json
		api_folder_key:Transaction folder}
	r = requests.post(url = api_endpoint, data = data)
	paste_url = r.text
	block_number = block_number + 1
	#if an error occurs that prevents Coinbot from reblogging a mined block, then it defaults to the second reblog and adds a note tagging the user, saying that the user tried to reblog Coinbot's block but Coinbot got an [insert error] message indicating that [thing happened]. 

#post the text stored in the transaction_list variable to Pastebin
def paste_transactions(Transactions):	
	api_endpoint = https://pastebin.com/api/api_post.php
	pastebin_key = api key
	Coinbot_user_key = pastebin_user_key
	paste_name = ("Transaction List: " + datetime.datetime.now())
	data = {api_dev_key:pastebin_key
		api_option:paste
		api_paste_code:transaction_list
		api_user_key:Coinbot_user_key
		api_paste_name:paste_name
		api_paste_format:json
		api_folder_key:Transaction folder}
	r = requests.post(url = api_endpoint, data = data)
	paste_url = r.text
	Transactions = {}

#define function for the bot to find its way through the thread to the most recent valid block of the chain (if it crashes, for example)
def restart_thread():
	URL = "api.tumblr.com/v2/blog/coinbot9000/posts/?api_key={key}&tag=valid_block"
	parameters = {}
	r = requests.get(url = URL, params = parameters)
	data = r.json()
	chain_length = data["response"]["total_posts"]
	get_block_one
	next_block = Masterpost_id
	while i <= (chain_length - 1):
		block_pair(next_block)
	URL = "api.tumblr.com/v2/blog/coinbot9000/posts/?api_key={key}"
	parameters = {"tag":valid_block}
	r = requests.get(url = URL, params = parameters)
	data = r.json()
	last_block = data["response"]["posts"][0][post_id]
	if next_block != last_block
		troubleshoot
	first_reblog(next_block)

#initializing functions
get_block_one()
Users = {}
coinbot_id = User(coinbot_id, Coinbot9000, 1000)
Users.append(coinbot_id)

#main loop
find_transactions()
first_reblog()
#wait 15 mins?
