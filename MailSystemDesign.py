"""
Hattori is very much inspired by the way GMAIL works. He decides to build his own simple version of GMAIL. He divides the mails into 3 categories ,namely : UNREAD , READ and TRASH.
UNREAD:the messages that haven't been read. 
READ:The messages that is read by the user.
TRASH: The messages deleted by the user.
Now, At any point of time, The user can READ an UNREAD message , Move an UNREAD message to TRASH , Move a READ message to TRASH or restore a deleted message back to READ category. Now , Hattori requires your help in determining the messages left in all the categories aligned in the order of their arrival in that category.
Formally: You are given N messages , with ID from 1 to N. Initially all the messages are in the UNREAD section of the mail.Now, Q queries are given in the form as shown below:
1 X : Move the message with ID X from UNREAD to READ.
2 X : Move the message with ID X from READ to TRASH.
3 X : Move the message with ID X from UNREAD to TRASH.
4 X : Move the message with ID X from TRASH to READ.
Given that all the queries are valid, Help Hattori in Determining the messages in all the 3 sections.

Input:
First line contains the number of test cases. First line of each test case contains two space separated values N and Q respectively. Second line contains 2*Q integers each either of the form as described above. 

Output:
First line contains all the space seperated message ID'S left in the UNREAD section.
Second line contains all the space seperated message ID'S left in the READ section.
Third line contains all the space seperated message ID'S left in the TRASH section.
NOTE: In case, any section is empty , print "EMPTY" for that section without double quotes.

Constraints:
1<=T<=20
1<=N<=5000
1<=Q<=10^6

Example:
Input:
1
10 7
1 2 1 5 1 7 1 9 2 5 2 7 4 5
Output:
1 3 4 6 8 10 
2 9 5 
7

Explaination:
Initial UNREAD section: 1->2->3->4->5->6->7->8->9->10
READ section : EMPTY
TRASH section : Empty
Query 1 : 1 2
UNREAD section: 1->3->4->5->6->7->8->9->10
READ section : 2
TRASH section : Empty
Query 2 : 1 5
UNREAD section: 1->3->4->6->7->8->9->10
READ section : 2->5
TRASH section : Empty
Query 3 : 1 7
UNREAD section: 1->3->4->6->8->9->10
READ section : 2->5->7
TRASH section : Empty
Query 4 : 1 9
UNREAD section: 1->3->4->6->8->10
READ section : 2->5->7->9
TRASH section : Empty
Query 5 : 2 5
UNREAD section: 1->3->4->6->8->10
READ section : 2->7->9
TRASH section : 5
Query 6 : 2 7
UNREAD section: 1->3->4->6->8->10
READ section : 2->9
TRASH section : 5->7
Query 7 : 4 5
UNREAD section: 1->3->4->6->8->10
READ section : 2->9->5
TRASH section : 7
"""

import sys
from sys import stdin, stdout, stderr


def main():
    
    UNREAD = []
    READ = []
    TRASH = []

    finallist = list()
    testcount = int(input(""))
    for testcase in range(testcount):
        totalMsgs, msgCount = input("").split()
        msgList = input().split()
        totalMsgs = int(totalMsgs)
        msgCount = int(msgCount)
        for item in range(1, totalMsgs+1):
            UNREAD.append(str(item))
        MSGID = []
        ALLMSG = []
        for item in range(0, 2*msgCount, 2):
           ALLMSG.append(msgList[item+1])
           MSGID.append(msgList[item])
        for item in range(len(MSGID)):
            if MSGID[item] == '1' and ALLMSG[item] in UNREAD:
                READ.append(ALLMSG[item])
                UNREAD.remove(ALLMSG[item])
            elif MSGID[item] == '2' and ALLMSG[item] in READ:
                TRASH.append(ALLMSG[item])
                READ.remove(ALLMSG[item])
            elif MSGID[item] == '3' and ALLMSG[item] in UNREAD:
                TRASH.append(ALLMSG[item])
                UNREAD.remove(ALLMSG[item])
            elif MSGID[item] == '4' and ALLMSG[item] in TRASH:
                READ.append(ALLMSG[item])
                TRASH.remove(ALLMSG[item])


        for item in [UNREAD, READ, TRASH]:
            if len(item) == 0:
                print("EMPTY")
            else:
                print(" ".join(item))
        
if __name__ == "__main__":
    main()
    
