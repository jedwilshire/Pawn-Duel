# Pawn-Duel
A simple pawn duel game where players never want pawns abandoned!

Rules:   
Red player goes first.  
Each turn has three phases that proceed in this order:  
		1. Movement: The player selects (clicks on) a pawn of their color to move forward one space into a space that player does not currently occupy.  
		2. Capture: If player moves his/her pawn onto one of their opponents pawns, their opponent's pawn is captured.  
		3. Abandonment: If at the end of the movement and capture phases any pawns from either player are not within one space (horizontally, vertically, or diagonally) of a pawn matching their color, then that pawn is considered abandoned and is removed from the board.  
The first player to deliver a pawn to the opposite side of the board is the winner.  

Examples of abandonment:  
``..BBB``  
``..R..``  
``...R.``  
``.....``    
Currently, red has two pawns that are protecting each other.  If red moves the most forward pawn up 1 row to capture a blue pawn, then he/she will abandone both pawns, and both are removed.  The blue pawn was still captured as that occurs before abandonded pawns are removed.  
``..RBB     ...BB``  
``.....     .....``  
``...R.---->.....``   
``.....     .....``    
If instead red moves the back pawn forward both continue to protect each other.  
``..BBB``  
``..RR.``  
``.....``  
``.....``  
However, blue may now move one of his/her pawns down and capture a red pawn, which causes the other to be abandoned.  
``..B.B     ..B.B``    
``..RB.     ...B.``   
``.....---->.....``     
``.....     .....``     
