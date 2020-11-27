# CS 465 Homework 2
## Created By Rory O'Connor

There were a few key differences that differentiated this algorithm from other
poker algorithms.  First, there is less information available for the agent to 
make his decision compared to traditional poker.  This is because the Agent has
no way of knowing what cards were discarded by the other players. Additionally, 
there is no betting or raising in this version of poker.  Therefore, we only 
need to determine which cards, if any, provide us with the best odds of 
improving our hand if we discard them.  

I have decided upon the following strategy: 

    - I will first check if we have any hands which are likely to win.  These 
      include Straights, Flushes, 4-of-a-kind, 3-of-a-kind, If we have those we are just going to
      keep that hand, since they are high ranked. 
    
    - If we don't have a high value hand, we will find our highest pair and 
      keep those cards, and discard other unecessary cards in order to 
      maximize our chances of getting 3 of a kind.
    
    - If we don't have a pair, then we will discard all of our cards except for the highest in order to maximize
      the chances of getting at least a pair (hopefully 3 of a kind)

I chose to go for 3 of a kind because it is a hand which will beat most poker
hands, but is also not so rare that it will rarely come up.  While I could 
have attempted to target a hand with a higher value, like a royal flush, the 
state space is so large that there would be no guarantee that a better hand 
will come up.  Basically, three of a kind strikes the right balance between the 
likelihood that I will win with that hand and the probability that I will get 
the hand I want when I discard my cards.  Additionally, this algorithm has 
the added benefit of being very simple to remember, so if this algorithm
performs well against my fellow students then I will likely have an ideal 
strategy in order to win lots of money from my relatives over the holiday 
 
