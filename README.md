# pes_player-recommender

## What's the data? 
1. This is efootball pro evolusion soccer data,its got all the players across the world playing in different leagues and the entire performance measurees and individual special abilities like skill and rating in different position and finallly the overall rating.

## The philosophy is simple
1. Problem was how can i use this data in a way thats beneficial for a team thats facing some sort of challenge
1. This data does't contain any match statistics so i cannot use this to predict win probabilities or player selection for next match etc.
1. But another challenge often seen is to get players for low cost as a replacement for a player currently playing(often players playing in mediocre leagues or young players) but possessing a good talent and can fill the position of a player in the team
1. My intension is to make a player recomendation system very simply (probably i wont use  any clustering algorithms)

## Challenge
1. But getting a player and instantly making them play like an og player in football is not quite often so,
1. We can think of getting player who has a similar individual stats but this does't guarantee the requirements listed above(blending with the team philosophy and delivering a great performance)

## Solution
1. The problem really breaks down into the question of what a is team defined by
1. The team is often defined by the way they plays. a manager wants players that can fullfill the needs of his playin style
1. Sometimes a team is full of technical players, sometimes fast players, sometimes lot of attacking players, sometimes defensive and so on so,also the role of dirrent position in a tactical way changes in teams
1. My aproach is to make a vector that represents an individual team in feature space. the team is defined by the players playing, and different players are rated differently because of the individual contributions they have had in helping the team. (black ball, golden ,bronze and white in decreasing order of individual ability)
1. We can make a vector that represents the team as the weighted sum of all the players individual stats and then normalizing it with weight being the ball color.
1. Same way we can make a normalized vector that represents a perticular position in the team as the weighted sum of the players playing the perticular position.
1. Make a vector representing an indivudual player as the normalized individual stats
1. now i can analyze the euclidean distance which would represent the relationship between the player and different positions in the team and atlast to the antire team vector 
1. This is a nice way of understanding what a specific player mean to the team and finding players who has simlilar qualities we will end up getting players that play in small clubs but possess similar qualities and most importantly plays a similar role is  adifferent club