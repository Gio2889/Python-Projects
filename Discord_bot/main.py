
import discord
from discord.ext import commands
from datetime import datetime
bottoken='******'
myid='Bohique#2687'
client = discord.Client(intents = discord.Intents(messages=True,message_content=True, guilds=True,members=True))

##################### data managemet 
#%% 
import pandas as pd 
import numpy as np 
#script_directory = os.path.dirname(os.path.realpath(__file__))
#os.chdir(script_directory)
auditdata=pd.read_csv('audit_logs_K&K Anime2.txt',sep=',',names=['User','User ID','Action','Target','Target ID', 'Time'])
auditdata['User']=auditdata['User'].str.replace("b'","")
auditdata['Target ID']=auditdata['Target ID'].str.replace("'","")
auditdata['Time']=pd.to_datetime(auditdata['Time'])
#print(auditdata.info)
#print(auditdata.head())
auditdata.set_index('Time', inplace=True)
# Round the datetime objects down to the nearest day
auditdata.index = auditdata.index.floor('d')
auditdata=auditdata.loc['2022-12-16':'2022-12-18']
auditdata=auditdata[auditdata['User'] == 'Patreon#1968']
auditdata=auditdata[['Target','Target ID']]
#print(auditdata.head())
#print(auditdata.info)
makedict=0;
###############################################
#%%
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
     # Set the guild (server) object
    guild = client.guilds[0]
    print('Selected Server: '+ str(guild))
    member = guild.get_member('******')
    print('Selected Member: '+ str(member))
    print(str(member.name)+" "+ str(member.id))
    # Create a dictionary of Discord IDs to Discord usernames
    if makedict == 1:
        print('---Making id to user name dictiory---')
        id_to_username = {member.id: member.name for member in guild.members}
        with open(f'members_dictionary','w+') as f:
            for item in id_to_username.keys():
                f.write('ID is: '+str(item)+'; Username is: '+str(str(id_to_username[item]).encode('utf-8'))+'\n')
    


async def save_audit_logs(guild):
     with open(f'audit_logs_{guild.name}2.txt', 'w+') as f:
            async for entry in guild.audit_logs(limit=500):
                timestamp = str(entry.created_at)
                dt = datetime.fromisoformat(timestamp)
                #print(str(entry.user)+' '+str(type(entry.target)))
                if str(type(entry.user)) == "<class 'NoneType'>" or str(type(entry.target))  == "<class 'NoneType'>":
                    print('None entry found; skipping')
                    continue
                else:
                    frmtstr='{0.user},{0.user.id},{0.action},{0.target},{0.target.id}'.format(entry)
                    #f.write(str(str(entry).encode('utf-8'))+'\n')
                    f.write(str(frmtstr.encode('utf-8'))+','+str(dt)+'\n')
            f.write('EOF\n')

@client.event
async def on_message(message):
    print('----------------')
    print(f'{message.author.name} sent: {message.content}')
    print('----------------')
    if message.content.startswith('!auditlog'):
        # Check if the user has the "View Audit Log" permission
        if message.channel.permissions_for(message.author).view_audit_log:
            # Get the server's audit log
            print('obtaining server logs')
            await save_audit_logs(message.channel.guild)
            #       audit_log = message.guild.audit_logs(limit=100)
            #for entry in audit_log:
            #   print(f'{entry.user} made a {entry.action} on {entry.target}')
        else:
            await message.channel.send('You do not have permission to view the audit log.')
    elif  message.content.startswith('!roletest'):
         # Set the guild (server) object
        guild = client.guilds[0]
        print('Selected Server: '+ str(guild))
        # Set the role you want to modify
        role = discord.utils.get(guild.roles, name='Pro Heroes')
        print('Selected role: '+ str(role))
        #member = discord.utils.get(guild.members, name='Bohique')
        for mem in auditdata['Target ID']: 
            member = discord.utils.get(client.get_all_members(), id=int(mem))
            #member = guild.get_member(mem)
            #print('Selected Member: '+ str(member))
            #print(str(member.name)+" "+ str(member.id))
            # Modify the member's roles
            if role in member.roles:
                print(str(member.name) +' has role')
            else:
               print('Adding role to '+str(member.name))
               await member.add_roles(role)

client.run(bottoken)

# %%
