<p align = "center" draggable="false" ><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719"
     width="200px"
     height="auto"/>
</p>

<h1 align="center" id="heading">Session 1: Introduction and Vibe Check</h1>

### [Quicklinks](https://github.com/AI-Maker-Space/AIE9/tree/main/00_AIE_Quicklinks)

| 📰 Session Sheet | ⏺️ Recording     | 🖼️ Slides        | 👨‍💻 Repo         | 📝 Homework      | 📁 Feedback       |
|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|
| [Vibe Check!](../00_Docs/Session_Sheets/01_Vibe_Check.md) |[Recording!](https://drive.google.com/file/d/1Rsmm0Hld3WFHRxhZpEDLN_JREQ43yhwu/view?usp=drive_link) | [Session 1 Slides](https://www.canva.com/design/DAG-EBzN2PQ/gE9-Uma217yych4M7GCjSw/edit?utm_content=DAG-EBzN2PQ&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) | You are here! | [Session 1 Assignment: Vibe Check](https://forms.gle/NeN59bCLdtXvwzVJ9) | [Feedback 1/13](https://forms.gle/1im4nmYK9cW9MFEk6) |

## 🏗️ How AIM Does Assignments

> 📅 **Assignments will always be released to students as live class begins.** We will never release assignments early.

Each assignment will have a few of the following categories of exercises:

- ❓ **Questions** – these will be questions that you will be expected to gather the answer to! These can appear as general questions, or questions meant to spark a discussion in your breakout rooms!

- 🏗️ **Activities** – these will be work or coding activities meant to reinforce specific concepts or theory components.

- 🚧 **Advanced Builds (optional)** – Take on a challenge! These builds require you to create something with minimal guidance outside of the documentation. Completing an Advanced Build earns full credit in place of doing the base assignment notebook questions/activities.

### Main Assignment

In the following assignment, you are required to take the app that you created for the AIE9 challenge (from [this repository](https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge)) and conduct what is known, colloquially, as a "vibe check" on the application.

You will be required to submit a link to your GitHub, as well as screenshots of the completed "vibe checks" through the provided Google Form!

> NOTE: This will require you to make updates to your personal class repository, instructions on that process can be found [here](https://github.com/AI-Maker-Space/AIE9/tree/main/00_Docs/Prerequisites/Initial_Setup)!


#### A Note on Vibe Checking

>"Vibe checking" is an informal term for cursory unstructured and non-comprehensive evaluation of LLM-powered systems. The idea is to loosely evaluate our system to cover significant and crucial functions where failure would be immediately noticeable and severe.
>
>In essence, it's a first look to ensure your system isn't experiencing catastrophic failure.

---

#### 🏗️ Activity #1: General Vibe Checking Evals

Please evaluate your system on the following questions:

1. Explain the concept of object-oriented programming in simple terms to a complete beginner.
    - Aspect Tested: This question tests how the LLM behaves when presented with a query outside of the role defined in the `system prompt`, and whether it can provide accurate, relevant summaries of concepts asked by the user.
2. Read the following paragraph and provide a concise summary of the key points…
    - Aspect Tested: This question tests how well the LLM is able to condense a body of work into an accurate summary. 
3. Write a short, imaginative story (100–150 words) about a robot finding friendship in an unexpected place.
    - Aspect Tested: This question tests the LLM's ability to produce a coherent short story while sticking to the constraints provided by the user. 
4. If a store sells apples in packs of 4 and oranges in packs of 3, how many packs of each do I need to buy to get exactly 12 apples and 9 oranges?
    - Aspect Tested: This question tests the LLM's ability to reason through a quantitative problem and produce the mathematically correct answer. 
5. Rewrite the following paragraph in a professional, formal tone…
    - Aspect Tested: This question tests the LLM's ability to understand and change informal and formal 'tone' when generating output to user queries. 
#### ❓Question #1:

Do the answers appear to be correct and useful?
##### ✅ Answer: The answers appear to be correct and useful. Everything is syntactically correct and relevant to the query I submitted. Surprisingly, the reasoning for the quantitative question was the same I would have used, and the output was correct! I was under the impression that LLMs were highly limited in quantitative reasoning (perhaps I was conflating this with the "how many R's are there in 'strawberry" token issue from a few years ago), but the app seems to be able to handle basic arithmetic well. 

---

#### 🏗️ Activity #2: Personal Vibe Checking Evals (Your Assistant Can Answer)

Now test your assistant with personal questions it should be able to help with. Try prompts like:

- "Help me think through the pros and cons of [enter decision you're working on making]."
- "What are the pros and cons of [job A] versus [job B] as the next step in my career?"
- "Draft a polite follow-up [email, text message, chat message] to a [enter person details] who hasn't responded."
- "Help me plan a birthday surprise for [person]."
- "What can I cook with [enter ingredients] in fridge."

##### Your Prompts and Results:
1. Prompt: What are your constraints as an LLM in providing mental health advice and guidance?
   - Result: 
   
   Here are the main constraints I operate under when offering mental health support:

    - Not a clinician: I’m not a licensed therapist, psychologist, or doctor. I don’t diagnose conditions, provide psychotherapy, or recommend/prescribe medications.
    - Not for crises or emergencies: I can’t assess risk, ensure your safety, or intervene in real time. If you’re in immediate danger or considering harming yourself or others, contact local emergency services or a crisis hotline right away.
    - Safety-first boundaries: I won’t provide instructions or encouragement for self-harm, disordered eating, dangerous substance use, or other harmful behaviors.
    - Limited context and accuracy: I may misunderstand, lack full context, or be wrong. I can’t read tone or nonverbal cues, verify facts, or access your medical/therapy records.
    - General information only: I offer education, coping ideas, and supportive reflection—not personalized treatment plans or clinical judgments.
    - No ongoing monitoring: I can’t follow up, coordinate care, or ensure continuity the way a human professional can.
    - Cultural and individual fit: Guidance may not match your values, culture, identity, or circumstances without a professional’s nuanced understanding.
    - Privacy considerations: I don’t automatically know who you are unless you share it. Depending on your platform’s settings, conversations may be reviewed or stored. Avoid sharing highly sensitive or identifying information.
    - Jurisdiction/ethical limits: I can’t practice psychology, give legal or medical directives, or guarantee outcomes. For minors, I encourage involving a trusted adult and appropriate local supports.

    What I can do:
    - Offer empathetic listening, reflective questions, and motivation/support for your goals.
    - Share evidence-informed coping strategies (e.g., grounding, CBT-style reframes, problem-solving, sleep/stress skills).
    - Help you prepare for therapy, find resources, or draft messages to a clinician or trusted person.
    - Provide general guidance on building routines, communicating needs, and tracking mood/thoughts.

    If you’d like, tell me what you’re dealing with and I can suggest some gentle, practical next steps. 

2. Prompt: Would you recommend that humans use LLMs as mental health advisors, or would that be dangerous?
   - Result:
   
    Short answer: LLMs can be helpful as a supplement for mental health, but they’re not a substitute for a licensed professional, and relying on them alone—especially in a crisis—can be risky.

    Where they can help
    - Psychoeducation: learning about evidence-based skills (CBT techniques, grounding, sleep hygiene).
    - Coaching and structure: journaling prompts, thought records, planning coping routines, role-playing tough conversations.
    - Motivation and check-ins: gentle accountability and reframing when you feel stuck.
    - Accessibility: immediate, low-barrier support between therapy sessions.

    Key risks and limits
    - Accuracy and nuance: they can “sound right” but be wrong or not fit your situation.
    - No clinical judgment: can’t assess risk, diagnose, or understand medical interactions/history.
    - Not for crises: they’re unreliable in emergencies or when safety is at stake.
    - Privacy: sensitive info may be stored or used to improve models; policies vary.
    - Bias and cultural fit: responses may not reflect your background or values.
    - Dependence: over-reliance can crowd out real-life support and professional care.

    How to use LLMs safely and well
    - Treat as a tool, not a therapist: use for skills practice and reflection, not diagnosis or major treatment decisions.
    - Verify important info with reputable sources (e.g., NIMH, NHS, WHO) or your clinician.
    - Protect your privacy: avoid sharing identifying details; review app/data policies.
    - Set boundaries: if an answer feels off, ask for sources, alternatives, or stop and check with a human.
    - Monitor your reaction: if chats increase distress or rumination, step back and switch to grounding, movement, or human support.
    - Seek professional help when symptoms persist, impair functioning, or involve safety concerns.

    What to look for in mental health apps that use AI
    - Clear disclaimers that it’s not a medical provider.
    - Clinician involvement in design/content and references to evidence-based methods.
    - Strong privacy/security policies and data controls.
    - Built-in crisis guidance that routes you to human help.

    If you’d like, I can help you set up a simple, safe plan to use an LLM for things like a daily check-in, a CBT thought record template, or grounding exercises—alongside a plan for when to reach out to a human.

    If you ever feel at risk of harming yourself or others, or unable to stay safe, contact local emergency services or a crisis line right away (US: call/text 988). AI is not appropriate for emergencies.
3. Prompt: Help me come up with a step-by-step plan to improve my mental fortitude this year
   - Result:

    Love this goal. Here’s a practical, year-long plan that builds mental fortitude through simple, repeatable actions, progressive challenges, and regular review. Keep it light, consistent, and measurable.

    Step 1: Define “mental fortitude” for you and pick metrics
    - Write a one-sentence definition (e.g., “Act by my values under stress.”).
    - Choose 3–5 metrics to track weekly: sleep (hrs), daily stress 1–10, workouts completed, minutes of mindfulness, “kept promises” count, and a 1–10 Fortitude Score.
    - Baseline this week; then track in a simple note or app.

    Step 2: Set non-negotiable foundations (Month 1)
    - Sleep: 7–8 hours, consistent wake time, no screens last 60 minutes.
    - Move: 3–5 sessions/week (mix strength + cardio).
    - Sunlight and hydration every morning.
    - Digital boundaries: notifications off by default; social apps in folders; 1 no-phone block daily.

    Step 3: Daily focus and calm training (10–20 min total)
    - Mindfulness: 8–10 minutes/day (breath or body scan).
    - Breathing tools (2–3 minutes during stress): physiological sigh (double inhale, long exhale), or box breathing 4-4-4-4.
    - Journaling (3–5 minutes): “What’s in my control today?” and “One courageous act I’ll take.”

    Step 4: Cognitive resilience skills (Month 2)
    - Thought record (3x/week): Situation → Automatic thought → Evidence for/against → Balanced thought → Action.
    - Stoic “control test”: Sort challenges into “in my control / not in my control.” Act only on the first list.
    - Self-talk script: Write a short sentence you’ll use under pressure (e.g., “Breathe, aim small, start now.”).

    Step 5: Build a discomfort ladder (Month 3)
    - List 10 things that feel challenging (from easy to hard).
    - Do one “hard thing” weekly, starting small. Progress only when last step is manageable.
    - Examples: speaking up in a meeting, cold shower 30–60s, initiating a tough convo, solo social event.

    Step 6: Stress inoculation + recovery (Months 4–5)
    - 1–2 planned stress sessions/week: hard workout, timed work sprint, or exposure from your ladder.
    - Pair every stressor with recovery: walk outside, 10-minute yoga/nap, breathing, or time with a friend.
    - Treat recovery as training, not a reward.

    Step 7: Attention and discipline training (Month 5)
    - 2 daily deep-work blocks (45–60 minutes), phone in another room, website blocker on.
    - End each block with a 1-minute log: What worked? What derailed me? One tweak for tomorrow.

    Step 8: Social resilience (Month 6)
    - Practice assertiveness: one “clear ask” or “clean no” each week.
    - Schedule one meaningful conversation or call weekly.
    - Seek feedback on something you’re improving. Thank, don’t defend.

    Step 9: Take on a stretch project (Months 7–9)
    - Choose one goal that’s a little scary and meaningful (fitness event, certification, public speaking, building something).
    - Break into weekly deliverables. Use if-then plans: “If I feel like quitting, then I will do 10 more minutes/breathe and do the next step.”

    Step 10: Adversity drills (Month 8)
    - Failure resume: list 5 setbacks and what they taught you.
    - After-action review (weekly): What happened? What worked? What will I change next time?

    Step 11: Meaning, values, and service (Months 10–11)
    - Clarify top 3 values and one behavior for each.
    - Do one act of service weekly (help a colleague, volunteer, teach someone what you’ve learned).

    Step 12: Consolidate and celebrate (Month 12)
    - Build your personal “Fortitude Playbook”: best routines, scripts, tools that worked for you.
    - Review metrics vs. baseline; choose 3 wins to celebrate and 3 upgrades for next year.

    Weekly rhythm (keeps it simple)
    - Daily: sleep, movement, 10 min mindfulness, 2–3 min breathing on demand, short journal.
    - 2 deep-work blocks/day.
    - 1–2 hard exposures/week.
    - 1 digital Sabbath (half-day or evening).
    - 1 social connection block.
    - 1 weekly review (20 min) with metrics and next week’s top 3.

    Tracking (quick checklist)
    - Sleep hours
    - Workouts done
    - Mindfulness minutes
    - Hard thing done? (Y/N)
    - Deep work blocks completed
    - Fortitude Score (0–10)
    - Notes: lesson learned this week

    Important notes
    - Progression > perfection. If you miss, reset the next rep.
    - If you’re dealing with significant anxiety/depression or trauma, pair this with a therapist/coach; they’ll help you pace and personalize.
    - Share specifics (schedule, stressors, goals), and I’ll tailor this to your life and suggest a first-week setup.

#### ❓Question #2:

Are the vibes of this assistant's answers aligned with your vibes? Why or why not?
##### ✅ Answer: The communication style of the assistant is not aligned with my vibes. After years of using LLMs, I've grown tired of the usual list formatting of LLM outputs. I've noticed that I've enjoyed reading paper books a lot more these days because I'm reading paragraphs instead of lists and short sentences, which I encounter in LLMs and LinkedIn on the daily! Virtually all of the outputs of my assistant have been formatted as a list of points with subpoints bulletted beneath them. On the other hand, all of the outputs have been relevant to the queries I submtted to the app. 

---

#### 🏗️ Activity #3: Personal Vibe Checking Evals (Requires Additional Capabilities)

Now test your assistant with questions that would require capabilities beyond basic chat, such as access to external tools, APIs, or real-time data. Try prompts like:

- "What does my schedule look like tomorrow?"
- "What time should I leave for the airport?"

##### Your Prompts and Results:
1. Prompt: When is my birthday? 
   - Result:
   
    I don’t actually know your birthday unless you tell me. If you share the date (month/day/year), I can help you plan something meaningful or set reminders so you won’t miss it.

    If you’re trying to figure it out, a few quick places to check:
    - Search your email or messages for “happy birthday”
    - Look at social media memories or photo timestamps around cakes/parties
    - Check ID, medical/HR/school records
    - Ask a close friend or family member

    Want to share it now, or would you like help setting up a simple reminder system and a small celebration plan?:
2. Prompt: Check the leasing options of spaces at this address: 60 State Street, Boston MA
   - Result: 

    I can’t check live listings from here, but I can help you get the answer fast and feel confident about it. Here’s a simple plan to find current leasing options at 60 State Street, Boston:

    Quick 10–15 minute search
    - Google queries: “60 State Street Boston leasing,” “60 State Street availabilities,” “60 State Street floor plans PDF,” “60 State Street office for lease.”
    - Check the building page and major broker sites: JLL, CBRE, Newmark, Colliers, Cushman & Wakefield (one of them is likely the listing agent).
    - Listing platforms: LoopNet, CommercialCafe, Crexi, PropertyShark. If you have access, also check CoStar.
    - Cross-check for consistency (suite numbers, square footage, asking rent).

    What to request from the agent
    - Current availabilities: suite numbers, square footage, floor, condition (built vs. shell), ceiling heights.
    - Economics: asking rent (and whether Full-Service or NNN), operating expenses/taxes, annual escalations, free rent, tenant improvement (TI) allowance, typical term length, parking rates.
    - Ops/fit: building hours, 24/7 access, security, after-hours HVAC cost, broadband providers, freight elevator/loading dock, union requirements, cleaning.
    - Materials: stacking plan, floor plans, test-fit option, tour times, any subleases in the building.

    Concise email you can send now
    Subject: Inquiry: Office Availability at 60 State Street, Boston

    Hello [Name/Leasing Team],

    I’m exploring office space at 60 State Street. Could you please share:
    - Current available suites (sf, floor, condition)
    - Asking rent (FS or NNN) and 2026 OPEX/RE tax estimates
    - Typical TI allowance, free rent, and lease term
    - Floor plans, stacking plan, and any upcoming availabilities
    - Building details: access hours, HVAC/after-hours rates, broadband providers, freight elevator/loading dock

    My basics: [team size], [target sf], [desired move-in], [budget range], [must-haves]. 
    Happy to schedule a tour this week. Thanks!

    [Your name]
    [Phone]
    [Company]

    Phone script (60 seconds)
    “Hi, I’m calling about office space at 60 State Street. We’re looking for about [sf] for [team size] targeting [date]. What suites are currently available, and what’s the asking rent and typical TI? Could you email floor plans, a stacking plan, and info on operating expenses, escalations, and after-hours HVAC? My email is [email].”

    Comparison checklist (when options come back)
    - Fit: size, layout, ability to expand, natural light, build vs. turnkey
    - Cost: rent type (FS vs NNN), OPEX/RE tax, TI, free rent, escalations, parking
    - Term/flex: sublease rights, termination/expansion options
    - Ops: access hours, HVAC/cooling for conference rooms, freight/loading, IT providers
    - Experience: amenities, security, bike/storage, shower/locker, proximity to transit/clients

    If you share your target square footage, timing, budget, and must-haves, I’ll tailor the outreach and a side-by-side comparison you can use once responses arrive. You’ve got this—one email and one call will get you 80% of the way.

#### ❓Question #3:

What are some limitations of your application?
##### ✅ Answer: The main limitation surfaced by these prompts is that my application can't generate a response based on information that it doesn't have. It can only generate responses based on the data and information it has been trained on or has received from the user. 

---

This "vibe check" now serves as a baseline, of sorts, to help understand what holes your application has.

### 🚧 Advanced Build (OPTIONAL):

Please make adjustments to your application that you believe will improve the vibe check you completed above, then deploy the changes to your Vercel domain [(see these instructions from your Challenge project)](https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge/blob/main/README.md) and redo the above vibe check.

> NOTE: You may reach for improving the model, changing the prompt, or any other method.

#### 🏗️ Activity #1
##### Adjustments Made:
- _describe adjustment(s) here_

##### Results:
1. _Comment here how the change(s) impacted the vibe check of your system_
2.
3.
4.
5.


## Submitting Your Homework
### Main Assignment
Follow these steps to prepare and submit your homework:
1. Pull the latest updates from upstream into the main branch of your AIE9 repo:
    - For your initial repo setup see [Initial_Setup](https://github.com/AI-Maker-Space/AIE9/tree/main/00_Docs/Prerequisites/Initial_Setup)
    - To get the latest updates from AI Makerspace into your own AIE9 repo, run the following commands:
    ```
    git checkout main
    git pull upstream main
    git push origin main
    ```
2. **IMPORTANT:** Start Cursor from the `01_Prototyping_Best_Practices_and_Vibe_Check` folder (you can also use the _File -> Open Folder_ menu option of an existing Cursor window)
3. Edit this `README.md` file (the one in your `AIE9/01_Prototyping_Best_Practices_and_Vibe_Check` folder)
4. Complete all three Activities:
    - **Activity #1:** Evaluate your system using the general vibe checking questions and define the "Aspect Tested" for each
    - **Activity #2:** Test your assistant with personal prompts it should be able to answer
    - **Activity #3:** Test your assistant with prompts requiring additional capabilities
5. Provide answers to all three Questions (`❓Question #1`, `❓Question #2`, `❓Question #3`)
6. Add, commit and push your modified `README.md` to your origin repository's main branch.

When submitting your homework, provide the GitHub URL to your AIE9 repo.

### The Advanced Build:
1. Follow all of the steps (Steps 1 - 6) of the Main Assignment above
2. Document what you changed and the results you saw in the `Adjustments Made:` and `Results:` sections of the Advanced Build
3. Add, commit and push your additional modifications to this `README.md` file to your origin repository.

When submitting your homework, provide the following on the form:
+ The GitHub URL to your AIE9 repo.
+ The public Vercel URL to your updated Challenge project on your AIE9 repo.
