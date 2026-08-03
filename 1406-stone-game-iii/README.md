<h2><a href="https://leetcode.com/problems/stone-game-iii">1406. Stone Game III</a></h2><h3>Hard</h3><hr><p>Alice and Bob continue their games with piles of stones. There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array <code>stoneValue</code>.</p>

<p>Alice and Bob take turns, with <strong>Alice starting first</strong>. On each player's turn, that player can take <strong>1, 2, or 3 stones</strong> from the first remaining stones in the row.</p>

<p>The score of each player is the sum of the values of the stones taken. The score of each player is 0 initially.</p>

<p>The objective of the game is to end with the highest score, and the winner is the player with the highest score who there could be a tie. The game continues until all the stones have been taken.</p>

<p>Assume Alice and Bob play <strong>optimally</strong>.</p>

<p>Return <code>"Alice"</code><em> if Alice wins, </em><code>"Bob"</code><em> if Bob wins, or </em><code>"Tie"</code><em> if they get the same score</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> stoneValue = [1,2,3,7]
<strong>Output:</strong> "Bob"
<strong>Explanation:</strong> Alice will always lose. Her best move will be to take three piles and the score essential becomes 6. Now the score of Bob is 7 and Bob wins.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> stoneValue = [1,2,3,-1,-2,-3,7]
<strong>Output:</strong> "Alice"
<strong>Explanation:</strong> Alice choose two piles in the first move, her score is 1 + 2 = 3. Bob will choose 3 piles to get a score of 3 + (-1) + (-2) = 0.
Then Alice choose the next two piles, her total score becomes 3 + (-3) + 7 = 7.
Bob has no more piles to choose from, total score of Bob is 0.
Alice wins because 7 &gt; 0.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> stoneValue = [1,2,3,6]
<strong>Output:</strong> "Tie"
<strong>Explanation:</strong> Alice chooses the first 3 piles. Her score is 1 + 2 + 3 = 6. Bob chooses the last pile having a score of 6.
The game ends in a tie.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= stoneValue.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>-1000 &lt;= stoneValue[i] &lt;= 1000</code></li>
</ul>
