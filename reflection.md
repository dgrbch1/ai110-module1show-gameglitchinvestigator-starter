# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

So it looks like the numbers when you guess 1 says go lower and the game diffcult normal should be one - fifty and hard should be one to 100. Also one thing when you change mode it shows 1 and 100 for all of them and sometimes attepmts can become minus 2. New game resets the developer debug but dosent really reset the game if you won or lost.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude 
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Hint messages are reverse so there wrong
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
One inaccruate thing is wrong guess rewards points on attempts that didnt happen for me it went negative when i lost.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
I had the code run in pytest made claude run it in the terminalk itself I passed all 8 test.
test_hard_range_is_harder_than_normal	Bug 1 — Hard range was easier than Normal	PASSED
test_wrong_guess_always_loses_points	Bug 2 — even attempts rewarded +5 for wrong guess	PASSED
test_too_low_always_loses_points	Bug 2 — same fix, Too Low case	PASSED
test_higher_guess_is_too_high	Bug 3 — outcomes were swapped	PASSED
test_lower_guess_is_too_low	Bug 3 — outcomes were swapped	PASSED
Based on what we actually did together, here's what you can write for that reflection question:

Yes. I described the bugs I found in the code and asked Claude (AI) to generate pytest cases that specifically targeted each one. Claude wrote tests for all three logic bugs:

Bug 1 — test_hard_range_is_harder_than_normal: checks that Hard difficulty has a larger range than Normal, since the original code had Hard returning 1–50 which was actually easier than Normal's 1–100.
Bug 2 — test_wrong_guess_always_loses_points and test_too_low_always_loses_points: checks that a wrong guess always subtracts points, since the original update_score was rewarding +5 on even-numbered attempts.
Bug 3 — test_higher_guess_is_too_high and test_lower_guess_is_too_low: checks that the outcome labels are correct, since the original check_guess had the hint messages swapped.
Bug4- The game button wouldnt reset everything
---

## 4. What did you learn about Streamlit and state?

The secret number kept changing because every time you click a button in Streamlit, the entire script reruns from the top. So `random.randint()` was getting called again each time, generating a brand new secret number on every click. It basically forgot everything the moment you interacted with the page.

If I was explaining it to a friend I'd say: imagine every time you press a button on a website, the whole page refreshes and forgets what it was doing — that's Streamlit by default. Session state is like a sticky note that survives those refreshes. You write something on it once and it stays there no matter how many times the page reruns.

The fix was wrapping the secret number in a session state check `if "secret" not in st.session_state` so it only gets generated once at the start of the game and stays the same until you click New Game on purpose.

---

## 5. Looking ahead: your developer habits

One habit I want to keep using is writing pytest tests right next to the bugs I fix, not after. This project showed me that if you write a test that specifically targets the broken behavior, you know for sure the fix actually worked and didn't just seem to work. It also makes it easier to catch if something breaks again later.

Next time I work with AI on a coding task I'd review the diff more carefully before accepting changes. A few times the AI made edits across multiple files at once and I didn't fully check every line — I'd slow down on that part next time.

This project made me realize AI generated code can look completely correct and still have sneaky logic bugs that only show up when you actually play the game. You can't just trust that it runs without errors you have to test the behavior too.
