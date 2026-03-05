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

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
