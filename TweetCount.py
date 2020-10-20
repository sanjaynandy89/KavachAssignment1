class TweetCount:
    def __init__(self):
        self.tweets={}
        self.name=''
        self.tweetid=''
    def input(self,max):
        for i in range(max):
             #input name and tweet id
             self.name,self.tweetid=input().split()
             #store name and tweet in a dictionary 
             if self.name not in self.tweets.keys():
                 self.tweets[self.name]=[]
                 self.tweets[self.name].append(self.tweetid)
             else:
                 self.tweets[self.name].append(self.tweetid)
    def output(self):
        maxvalue=0
        maxkey=''
        final={}
        #store the name and number of tweet in a dictionary
        for key,values in self.tweets.items():
             final[key]=len(values)
        #find the maximum number of tweet     
        for key,values in final.items():
            if maxvalue<=values:
                maxvalue=values
        #print the user with maximum tweets        
        for key,values in sorted(final.items()):
            if values==maxvalue:
                 print('{} {}'.format(key,values))
#Number of test cases
N=int(input())
ob=[]
#create N objects for N test cases
for i in range(0,N):
  ob.append(TweetCount())
for obj in ob:
#store number of tweet in each test case   
    n=int(input())   
    obj.input(n)
for obj in ob:
    obj.output()

 
