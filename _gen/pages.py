"""Guide content for remireminder.app. Edit here, then run `python3 _gen/gen_site.py`.

FEATURE TRUTH (verified in the app source 2026-10-01, build 1.20). Every claim below maps to one of these.
If the app changes, re-check before editing copy: a guide that promises an unshipped feature draws
installs that churn.

- Three kinds of reminder: exact date (day + time), approximate (Anytime / Early / Mid / Late of a month),
  Someday (no date). Default month parts: Early 1-10, Mid 11-20, Late 21-end; presets in Settings
  (10/20, Balanced 9/18, 7/21).
- Only EXACT-date reminders send their own notification. Approximate and Someday reminders show up in
  the lists, Today, the calendars and widgets, plus an optional weekly and/or monthly summary
  notification (Settings > Notifications, both off by default).
- Repeats are PREMIUM. Exact-date: daily, weekly, every 2 weeks, monthly, custom every N days/weeks/months.
  Month-based: monthly, every 2 months, yearly, custom every N months/quarters/years. Ends: never, or
  after N times. (No end-date picker.)
- Planning more than 12 months ahead is PREMIUM.
- Views: Reminders list (Upcoming / Someday sections), Today, Yearly (12 months per screen, scrollable
  into next year), Month. Search.
- Home Screen widgets only (NO Lock Screen widgets): Today's Reminders (S/M/L), Mini Calendar (S),
  Next Month (S), Due Today (S), Overdue (S), Next 7 Days (S/M), Next 30 Days (L), Next 3 (S/M).
  Free: Today's Reminders + Mini Calendar. Premium: the other six.
- Voice input is PREMIUM: press and hold the + button, speak. Understands "early March", "mid-April",
  "end of July", "next month", "tomorrow", "every 3 months"/"quarterly", "every year"; a reminder with
  no date in it becomes Someday. Recognition runs on the device.
- Calendar sync: ONE-WAY, Remi to the system calendar. iCloud backup. No account. 24 accent colours
  (4 free). iOS 17.6 or later, iPhone.
- Price: free, Premium is a $6.99 one-time purchase (USD; local price varies).
- Repeat menu labels in the app: exact "Every day / Every week / Every 2 weeks / Every month / Custom…";
  month-based "Every month / Every 2 months / Every year / Custom…". Custom: 1-30 (exact) or 1-24 (month-based).

iOS CONTEXT (checked 2026-10-01 against Apple support 102484, MacRumors/9to5Mac iOS 26.2-27 coverage):
- iOS 26.2+: the built-in Reminders app can mark a reminder Urgent; it rings as an ALARM at its due time,
  through Silent and Focus, fixed 9-minute snooze. Never write "reminders can't ring on Silent" unqualified.
- iOS 27: natural-language entry in Reminders and Calendar, extra-large widget size. Still NO fuzzy dates
  (early/mid/late month) and no someday concept in the built-in apps.
- Built-in Reminders' exact repeat menu labels were NOT verified: describe them ("a monthly repeat"), don't quote.
- Alarm Clock Planner (cross-sell): dated alarms, monthly/yearly repeats, rings through Silent/Focus (AlarmKit),
  3 alarms free, REQUIRES iOS 26.2+ (say so; Remi runs from 17.6).
"""

# Cross-promotion targets: shipped, live apps only (brand rule: an unshipped project is not a product).
ALARMPLANNER = "https://alarmclockplanner.com/"
ALARM_RECURRING = "https://alarmclockplanner.com/guides/recurring-alarm-iphone/"
ALARM_SILENT = "https://alarmclockplanner.com/guides/iphone-alarm-silent-mode/"
ALARM_DATE = "https://alarmclockplanner.com/guides/set-alarm-for-specific-date-iphone/"
RISE = "https://risemorning.app/"

# Each cross-sell box: (heading, paragraph html). Shown only where the need genuinely differs.
XSELL_ALARM = ("Need it to actually ring?",
    f"""A Remi reminder is a regular notification: one sound at notification volume, no sound on Silent, and easy to swipe away. For a wake-up, a medication dose or anything you cannot miss, you want something that rings like an alarm. On iOS 26.2 and later, the built-in Reminders app can do that for a single reminder if you mark it <strong>Urgent</strong>. For alarms on real dates with monthly and yearly repeats, there is <a href="{ALARMPLANNER}" data-ph="xsell_alarmplanner">Alarm Clock Planner</a>, our alarm app: its alarms ring through Silent and Focus. It needs iOS 26.2 or later.""")

PAGES = [
# ---------------------------------------------------------------- 1
dict(
slug="reminder-without-date-iphone",
cluster="nodate",
title="How to Set a Reminder Without a Date on iPhone",
meta="Not everything has a deadline. How to save a reminder with no date on iPhone, and keep undated reminders where you will actually see them.",
h1="How to Set a Reminder Without a Date on iPhone",
lede="Fix the garden fence. Learn to make sourdough. Call that friend you keep meaning to call. None of these happen on a particular Tuesday, and pretending they do is how they end up ignored.",
quick="""<strong>Quick answer:</strong> In the built-in Reminders app, a reminder with no date is the default: just type it and leave the date off. The catch is that undated reminders sit in a list you only see when you go looking. <a href="/">Remi</a> gives them their own <em>Someday</em> section and, when you are ready, lets you move them to a loose time like "early March" instead of a hard date.""",
body="""
<h2>Undated reminders are allowed, they just disappear</h2>
<p>Most reminder apps on iPhone, including the built-in one, let you save a task without a due date. The problem is not saving it. The problem is that a reminder with no date never comes back to you on its own. It has no alert, it does not show in today's list, and it slowly sinks under everything that does have a date.</p>
<p>So people do the next obvious thing and give it a fake date, "this Saturday", just to make it appear somewhere. Saturday comes, the fence does not get fixed, the reminder goes overdue, and now it is a small red guilt badge instead of a plan.</p>

<h2>Give undated things a home, not a deadline</h2>
<p>The honest version of "I'll do it sometime" is a separate place for things that have no date yet, that you actually look at. In <a href="/">Remi</a> that place is <strong>Someday</strong>:</p>
<ol>
  <li>Tap the + button and type the reminder.</li>
  <li>Switch on <strong>Don't have a concrete date in mind?</strong></li>
  <li>Save. It goes into the Someday section of your reminders list, below everything that is coming up.</li>
</ol>
<figure>
  <img class="screen" src="/assets/guides/someday.webp" alt="Remi reminder list with an Upcoming section and a Someday section holding undated reminders like Visit Lisbon and Fix the garden fence" loading="lazy" width="640" height="1284">
  <figcaption>Upcoming on top, Someday underneath. Undated does not mean forgotten.</figcaption>
</figure>

<h2>When "someday" gets closer, give it a rough time</h2>
<p>Most undated tasks eventually firm up a little. Not to a day, but to a stretch of time: "before winter", "early next month", "sometime in spring". Remi has a middle step for exactly that. Open the reminder and pick <strong>Early</strong>, <strong>Mid</strong> or <strong>Late</strong> of a month, or <strong>Anytime</strong> that month. It moves out of Someday and into your upcoming list, without inventing a deadline you will just miss. More on that in <a href="/guides/remind-me-sometime-next-month/">reminders for sometime next month</a>.</p>

<h2>Do undated reminders send notifications?</h2>
<p>No, and they should not. A notification needs a moment to fire, and the whole point is that there is no moment yet. In Remi you see them whenever you open the list, and you can turn on a weekly or monthly summary notification in Settings that gives you a nudge about what is coming up.</p>
""",
faqs=[
 ("Can you make a reminder without a date on iPhone?", "Yes. Both the built-in Reminders app and Remi let you save a reminder with no date. In Remi, switch on \"Don't have a concrete date in mind?\" and it goes into the Someday section of your list."),
 ("Will a reminder with no date ever notify me?", "Not on its own, because there is no time for it to fire. In Remi it stays visible in your Someday list, and an optional weekly or monthly summary notification reminds you to look."),
],
related=["someday-maybe-list-iphone", "remind-me-sometime-next-month", "adhd-reminder-app"],
cta_h="A home for the things without a date",
cta_p="Free on iPhone. No account needed.",
),
# ---------------------------------------------------------------- 2
dict(
slug="someday-maybe-list-iphone",
cluster="nodate",
title="How to Keep a Someday/Maybe List on iPhone",
meta="A someday/maybe list keeps ideas out of your head and out of today's to-do list. How to run one on iPhone, review it, and move items out when they become real.",
h1="How to Keep a Someday/Maybe List on iPhone",
lede="Some ideas are not tasks yet. Visit Lisbon. Read War and Peace. Learn the guitar properly this time. They deserve to be written down, just not next to 'buy milk'.",
quick="""<strong>Quick answer:</strong> Keep a separate list for things you might do one day, look at it every week or two, and promote items out of it when they become real. On iPhone you can do this with a dedicated list in any reminders app. <a href="/">Remi</a> builds it in: undated reminders live in a <em>Someday</em> section, and you move one forward by giving it a month, or a rough part of one.""",
body="""
<h2>What a someday/maybe list is for</h2>
<p>The idea comes from the productivity world, but it is simple: anything you might want to do, but are not committing to now, goes on one list. It gets the thought out of your head, so you stop re-remembering it at 2am, and it keeps your real to-do list short enough to trust.</p>
<p>The list only works if two things are true: it is easy to add to, and you actually look at it now and then. A someday list you never open is just a nicer way of forgetting.</p>

<h2>Setting one up</h2>
<p>With a general reminders app, create a list called Someday and add to it. In <a href="/">Remi</a> you do not need a separate list: any reminder saved without a date goes into the <strong>Someday</strong> section automatically, below what is coming up.</p>
<ol>
  <li>Tap + and type the idea.</li>
  <li>Switch on <strong>Don't have a concrete date in mind?</strong> and save.</li>
  <li>With Premium you can also press and hold + and just say it. Anything you say without a date, like "visit Lisbon", is saved as Someday.</li>
</ol>
<figure>
  <img class="screen" src="/assets/guides/someday.webp" alt="Someday section in Remi listing Learn to make sourdough, Visit Lisbon, Fix the garden fence, Read War and Peace and Call my old roommate" loading="lazy" width="640" height="1284">
  <figcaption>The Someday section sits under your upcoming reminders, out of the way but one scroll from view.</figcaption>
</figure>

<h2>Reviewing it without it becoming a chore</h2>
<p>Pick a low-stakes moment, a Sunday coffee or the first of the month, and scroll through Someday. For each item, one of three things:</p>
<ul>
  <li><strong>Still a maybe.</strong> Leave it.</li>
  <li><strong>Getting real.</strong> Give it a month, or Early, Mid or Late of a month. It moves up into your upcoming reminders.</li>
  <li><strong>No longer interested.</strong> Delete it, guilt-free. Dropping an idea is a decision, not a failure.</li>
</ul>
<p>A monthly summary notification (Settings &gt; Notifications) is a good prompt for that review.</p>

<h2>Why not just give everything a date?</h2>
<p>Because a fake date turns a wish into an overdue task. "Visit Lisbon by June 1" will be overdue on June 2, and an overdue list full of things you never committed to teaches you to ignore the list. Keeping maybes undated until they are real keeps your dated reminders honest.</p>
""",
faqs=[
 ("What is a someday/maybe list?", "A list of things you might do one day but are not committing to now. It keeps ideas out of your head and off your active to-do list, and you review it now and then to promote, keep or drop items."),
 ("How do I move a someday item to a real date in Remi?", "Open the reminder and pick a month, or Early, Mid or Late of a month, or an exact date. It leaves the Someday section and appears in your upcoming reminders."),
],
related=["reminder-without-date-iphone", "plan-your-year-iphone", "voice-reminder-iphone"],
cta_h="Write the maybes down, keep today clean",
cta_p="Free on iPhone. No account, no subscription.",
),
# ---------------------------------------------------------------- 3
dict(
slug="remind-me-sometime-next-month",
cluster="nodate",
title="How to Set a Reminder for Sometime Next Month on iPhone",
meta="Some tasks belong to a part of the month, not a day. How to set a reminder for early, mid or late next month on iPhone without inventing a fake deadline.",
h1="How to Set a Reminder for Sometime Next Month",
lede="Renew the passport, early November. Book the dentist, mid-month. Clean out the garage, before the month is out. You know roughly when. You do not know the day, and you should not have to.",
quick="""<strong>Quick answer:</strong> Calendar apps and the built-in Reminders app need a specific day, so "sometime next month" usually becomes the 1st, and then it is overdue on the 2nd. <a href="/">Remi</a> lets you pick <strong>Early</strong>, <strong>Mid</strong> or <strong>Late</strong> of a month, or <strong>Anytime</strong> that month, and shows the reminder for that whole stretch.""",
body="""
<h2>The problem with picking a day you made up</h2>
<p>When an app insists on a date, you pick one. Usually the 1st, or the next Saturday. The task was never really due then, so you do not do it then, and it goes overdue. A few rounds of that and the reminders list is mostly red, and red stops meaning anything.</p>

<h2>Early, Mid, Late, or Anytime</h2>
<p>In <a href="/">Remi</a>, every reminder has a <em>When</em>. Besides an exact date, you can choose a part of a month:</p>
<ul>
  <li><strong>Early</strong> is the 1st to the 10th.</li>
  <li><strong>Mid</strong> is the 11th to the 20th.</li>
  <li><strong>Late</strong> is the 21st to the end of the month.</li>
  <li><strong>Anytime</strong> is the whole month.</li>
</ul>
<p>If your month runs differently, Settings has other splits, for example 1 to 7, 8 to 21 and 22 onward.</p>
<figure>
  <img class="screen" src="/assets/guides/create-approx.webp" alt="New reminder in Remi named Renew passport with When set to Early and Month set to November, highlighting the 1st to the 10th on the calendar" loading="lazy" width="640" height="1284">
  <figcaption>Early November, highlighted on the calendar: the 1st to the 10th.</figcaption>
</figure>

<h2>How to set one</h2>
<ol>
  <li>Tap the + button and type the reminder.</li>
  <li>In <strong>When</strong>, pick Early, Mid, Late or Anytime.</li>
  <li>Pick the month and year, and save.</li>
</ol>
<p>The reminder now shows in your list as, say, <em>Early November 2026</em>, and appears in the Month and Yearly views across that stretch of days.</p>

<h2>Will it notify me?</h2>
<p>Approximate reminders do not fire a notification at a set time, because there is no set time. They show up in your lists, calendars and widgets for their whole window. If you want a push, turn on the weekly or monthly summary in Settings &gt; Notifications, or switch the reminder to an exact date once the day becomes clear.</p>
""",
faqs=[
 ("Can I set a reminder for early next month instead of a specific day?", "Not in apps that require a due date. In Remi, choose Early, Mid, Late or Anytime and a month. Early covers the 1st to the 10th by default, Mid the 11th to the 20th, and Late the 21st to the end of the month."),
 ("Can I change what counts as early, mid and late?", "Yes. Remi has a few presets in Settings, for example 1-10 / 11-20 / 21-end, or 1-7 / 8-21 / 22-end."),
],
related=["reminder-without-date-iphone", "monthly-reminder-iphone", "plan-your-year-iphone"],
cta_h="Reminders that match how loose your plans really are",
cta_p="Free on iPhone. Early, Mid and Late are in the free version.",
),
# ---------------------------------------------------------------- 4
dict(
slug="monthly-reminder-iphone",
cluster="repeat",
title="How to Set a Monthly Reminder on iPhone (Bills & Rent)",
meta="How to set a reminder that repeats every month on iPhone, on the same date or just sometime early in the month, for rent, bills and subscriptions.",
h1="How to Set a Monthly Reminder on iPhone",
lede="Rent at the start of the month. The card bill around the 15th. Checking the subscriptions before they renew. Monthly reminders are the most useful kind, and the most annoying to keep rebuilding.",
quick="""<strong>Quick answer:</strong> The built-in Reminders app can repeat a reminder monthly on a fixed date. If a fixed date fits, that works. If the task really belongs to <em>the start of the month</em> rather than the 3rd exactly, <a href="/">Remi</a> can repeat an <strong>Early</strong>, <strong>Mid</strong> or <strong>Late</strong> reminder every month, so it shows up for that whole stretch instead of going overdue on day one.""",
body="""
<h2>Fixed date or part of the month?</h2>
<p>Some monthly things have a hard date: a direct debit on the 1st, a payment due on the 15th. Others just need doing <em>around</em> a time: paying rent sometime in the first week, reviewing the budget mid-month. Remi handles both, and repeats are part of Premium.</p>

<h2>A monthly reminder on a fixed date</h2>
<ol>
  <li>Tap + and type the reminder, for example "Pay the card bill".</li>
  <li>Set <strong>When</strong> to Exact and pick the first date, and a time if you want a notification.</li>
  <li>Open <strong>Repeat</strong> and choose <strong>Every month</strong>.</li>
  <li>Optionally choose to end after a number of times, for a payment plan with a known length. Save.</li>
</ol>
<p>Exact-date reminders send a notification at their time, if notifications are on for that reminder.</p>

<h2>A monthly reminder for part of the month</h2>
<ol>
  <li>Tap + and type it, for example "Pay rent".</li>
  <li>Set <strong>When</strong> to Early, Mid or Late, and the starting month.</li>
  <li>Open <strong>Repeat</strong> and choose <strong>Every month</strong>, or <strong>Every 2 months</strong>.</li>
</ol>
<p>When you tick it off, Remi moves it to the next month on its own, so the list always shows the one coming up.</p>
<figure>
  <img class="screen" src="/assets/guides/list.webp" alt="Remi reminder list showing Pay rent repeating every month, Bin day every week, and Mum's birthday every 12 months" loading="lazy" width="640" height="1284">
  <figcaption>Pay rent, every month, without a fake due date.</figcaption>
</figure>

<h2>When a reminder is not enough</h2>
<p>A missed rent reminder is an awkward conversation. A missed medication dose is a different matter. For anything that has to get your attention at an exact time, even with the phone on Silent, you need something that rings like an alarm, not a regular reminder. See the box below.</p>
""",
faqs=[
 ("How do I make a reminder repeat every month on iPhone?", "In the built-in Reminders app, set a date and pick a monthly repeat. In Remi, set an exact date or Early, Mid or Late of a month, then choose Every month under Repeat. Repeats are part of Remi Premium."),
 ("Can a monthly reminder stop after a few months?", "Yes. In Remi you can end a repeat after a set number of times, which suits payment plans and short courses."),
],
xsell=XSELL_ALARM,
related=["quarterly-reminder-iphone", "yearly-reminder-iphone", "reminder-vs-alarm-iphone"],
cta_h="Monthly things, handled once",
cta_p="Repeats are part of Premium: one $6.99 purchase, no subscription.",
),
# ---------------------------------------------------------------- 5
dict(
slug="yearly-reminder-iphone",
cluster="repeat",
title="How to Set a Yearly Reminder on iPhone (Birthdays, Renewals)",
meta="Birthdays, car insurance, the annual check-up: how to set a reminder that repeats every year on iPhone, and how to plan more than twelve months ahead.",
h1="How to Set a Yearly Reminder on iPhone",
lede="Car insurance renews every March. The boiler wants a service every autumn. Mum's birthday is on the 12th, every year, whether or not you remember on the 11th.",
quick="""<strong>Quick answer:</strong> Set the reminder once and repeat it yearly. In <a href="/">Remi</a> you can do that on an exact date, like a birthday, or for a whole month, like "car insurance, sometime in March", so you get the reminder early enough to shop around.""",
body="""
<h2>Two kinds of yearly reminder</h2>
<p>A birthday or anniversary is a fixed day. A renewal or an annual check-up is more of a season: you want to be thinking about it during that month, not the evening before. Remi does both. Repeats are part of Premium.</p>

<h2>Exact date, every year (birthdays, anniversaries)</h2>
<ol>
  <li>Tap + and type it, for example "Mum's birthday".</li>
  <li>Set <strong>When</strong> to Exact, pick the date and the time you want the notification.</li>
  <li>Open <strong>Repeat</strong>, choose <strong>Custom</strong> and set it to every 12 months.</li>
</ol>
<p>Tip: set the time a day or two early in a separate reminder if you need to buy a present.</p>

<h2>A month, every year (renewals, services, check-ups)</h2>
<ol>
  <li>Tap + and type it, for example "Car insurance renewal".</li>
  <li>Set <strong>When</strong> to Anytime, or Early, Mid or Late, and pick the month.</li>
  <li>Open <strong>Repeat</strong> and choose <strong>Every year</strong>. Or Custom, for every 2 or 3 years.</li>
</ol>
<figure>
  <img class="screen" src="/assets/guides/yearly.webp" alt="Remi yearly view showing all twelve months of 2027 with reminder days highlighted in green" loading="lazy" width="640" height="1284">
  <figcaption>The Yearly view: every month at once, so renewals stop being surprises.</figcaption>
</figure>

<h2>Planning further than a year out</h2>
<p>The free version of Remi covers the next twelve months. Premium removes that limit, which matters for things like a passport that expires in three years or a car service every two years.</p>
""",
faqs=[
 ("How do I set a birthday reminder that repeats every year?", "In Remi, create an exact-date reminder on the birthday, then set Repeat to Custom, every 12 months. In the built-in Reminders app, set the date and pick a yearly repeat."),
 ("Can I get a yearly reminder for a month instead of a specific day?", "Yes, in Remi. Pick Anytime (or Early, Mid or Late) of the month and set Repeat to Every year. It suits renewals and annual check-ups that happen around a time rather than on a day."),
],
related=["monthly-reminder-iphone", "quarterly-reminder-iphone", "plan-your-year-iphone"],
cta_h="Every year, without rebuilding it every year",
cta_p="Free on iPhone. Repeats and long-range planning are part of Premium.",
),
# ---------------------------------------------------------------- 6
dict(
slug="quarterly-reminder-iphone",
cluster="repeat",
title="How to Set a Reminder Every 3 Months on iPhone",
meta="Water filters, quarterly taxes, contact lenses, seasonal chores: how to set a reminder that repeats every 3 months (or every 6) on iPhone.",
h1="How to Set a Reminder Every 3 Months on iPhone",
lede="Change the water filter. Pay the quarterly tax. Rotate the mattress. Every three months is long enough to forget completely and short enough that it matters.",
quick="""<strong>Quick answer:</strong> Set the first one and repeat it every 3 months. In <a href="/">Remi</a> you can repeat <strong>every quarter</strong> for a part of a month, like "early January, then every quarter", or every 3 months on an exact date. Say "every 3 months" or "quarterly" to the voice input and it sets the repeat for you.""",
body="""
<h2>Why quarterly reminders get lost</h2>
<p>Weekly and monthly things turn into habits. Three months is too long for that. By the time it comes round, you have no memory of when you last did it, which is exactly why filters go unchanged for a year.</p>

<h2>Every quarter, around a time of the month</h2>
<ol>
  <li>Tap + and type it, for example "Change the water filter".</li>
  <li>Set <strong>When</strong> to Early (or Mid, Late, Anytime) and the first month.</li>
  <li>Open <strong>Repeat</strong>, choose <strong>Custom</strong>, and set every 1 quarter. For twice a year, every 2 quarters.</li>
</ol>
<figure>
  <img class="screen" src="/assets/guides/someday.webp" alt="Remi list showing Change the water filter, every quarter, starting January 2027" loading="lazy" width="640" height="1284">
  <figcaption>"Every quarter · starts Jan 2027." When you tick it off, it moves to April.</figcaption>
</figure>

<h2>Every 3 months on an exact date</h2>
<ol>
  <li>Set <strong>When</strong> to Exact and pick the first date and time.</li>
  <li>Open <strong>Repeat</strong>, choose <strong>Custom</strong>, and set every 3 months.</li>
</ol>
<p>Use the exact version when a date matters, like a tax deadline, and the quarter version when it just needs doing that month. Repeats are part of Remi Premium.</p>
""",
faqs=[
 ("How do I set a reminder every 3 months on iPhone?", "In Remi, create the reminder, open Repeat, choose Custom and set every 3 months (exact date) or every 1 quarter (part of a month). The built-in Reminders app also has repeat options for reminders with a date."),
 ("Can I set a reminder every 6 months?", "Yes. In Remi, use Custom and set every 6 months, or every 2 quarters."),
],
related=["monthly-reminder-iphone", "yearly-reminder-iphone", "voice-reminder-iphone"],
cta_h="Set it once, stop wondering when you last did it",
cta_p="Repeats are part of Premium: one $6.99 purchase, no subscription.",
),
# ---------------------------------------------------------------- 7
dict(
slug="reminder-widget-iphone-home-screen",
cluster="see",
title="How to Put Reminders on Your iPhone Home Screen (Widgets)",
meta="How to add a reminders widget to your iPhone Home Screen, which widget to pick, and how to see upcoming and overdue reminders at a glance.",
h1="How to Put Reminders on Your iPhone Home Screen",
lede="The reminder you see forty times a day gets done. The one inside an app you open twice a week does not. A widget is the cheapest fix there is.",
quick="""<strong>Quick answer:</strong> Press and hold an empty spot on the Home Screen, tap <strong>Edit</strong>, then <strong>Add Widget</strong>, search for your reminders app, pick a size and tap Add Widget. <a href="/">Remi</a> has eight Home Screen widgets, from today's list to a mini calendar and an overdue counter.""",
body="""
<h2>How to add a widget</h2>
<ol>
  <li>Press and hold an empty area of the Home Screen until the icons jiggle.</li>
  <li>Tap <strong>Edit</strong> in the top corner, then <strong>Add Widget</strong>. (On iOS 17, tap the <strong>+</strong> in the top corner instead.)</li>
  <li>Search for <strong>Remi</strong> and swipe through the widgets.</li>
  <li>Tap <strong>Add Widget</strong>, drag it where you want it, and tap Done.</li>
</ol>

<h2>Which widget to pick</h2>
<ul>
  <li><strong>Today's Reminders</strong> (small, medium, large): what is on for today. Free.</li>
  <li><strong>Mini Calendar</strong> (small): this month, with reminder days marked. Free.</li>
  <li><strong>Next 3</strong> (small, medium): the next three things coming up.</li>
  <li><strong>Next 7 Days</strong> (small, medium) and <strong>Next 30 Days</strong> (large): a rolling look ahead.</li>
  <li><strong>Due Today</strong> and <strong>Overdue</strong> (small): a single number, for when you just want to know if anything is waiting.</li>
  <li><strong>Next Month</strong> (small): next month's calendar, for planning ahead.</li>
</ul>
<p>Today's Reminders and Mini Calendar are free. The other six come with Premium.</p>

<h2>A good starting setup</h2>
<p>A medium <strong>Today's Reminders</strong> on your first Home Screen and a small <strong>Mini Calendar</strong> next to it covers most people. If you tend to let things slide, add the small <strong>Overdue</strong> counter: one number is easier to face than a long list.</p>

<h2>What about the Lock Screen?</h2>
<p>Remi's widgets are for the Home Screen. It does not have Lock Screen widgets.</p>
""",
faqs=[
 ("How do I add a reminders widget to my iPhone Home Screen?", "Press and hold an empty spot on the Home Screen, tap Edit, then Add Widget, search for the app, choose a size and tap Add Widget."),
 ("Does Remi have widgets?", "Yes, eight Home Screen widgets: Today's Reminders, Mini Calendar, Next Month, Due Today, Overdue, Next 7 Days, Next 30 Days and Next 3. Today's Reminders and Mini Calendar are free."),
 ("Does Remi have Lock Screen widgets?", "No. Remi's widgets are for the Home Screen."),
],
related=["plan-your-year-iphone", "adhd-reminder-app", "monthly-reminder-iphone"],
cta_h="Put the next thing where you will see it",
cta_p="Free on iPhone. Two widgets free, all eight with Premium.",
),
# ---------------------------------------------------------------- 8
dict(
slug="adhd-reminder-app",
cluster="see",
title="ADHD-Friendly Reminders: Why Fake Deadlines Backfire",
meta="Most reminder apps force a date on everything. For many people with ADHD, fake due dates become an overdue list they stop opening. A calmer approach.",
h1="Reminders That Work With an ADHD Brain",
lede="If your reminders list is a wall of red you stopped opening months ago, the problem may not be you. It may be that the app made you promise dates you never meant.",
quick="""<strong>Quick answer:</strong> Keep reminders honest. Only give a hard date to things that really have one, give everything else a rough time ("late October") or no date at all, and keep the next thing visible on your Home Screen. That is the idea behind <a href="/">Remi</a>, a reminder app built around approximate dates and a Someday list.""",
body="""
<p class="note-box">This is a practical note on how reminder apps are designed, not medical advice. If ADHD is affecting your life, a professional is the right person to talk to.</p>

<h2>How fake deadlines turn into ignored lists</h2>
<p>Most reminder apps want a date. So you pick one: tomorrow, this weekend, the 1st. Many of those tasks were never really due then. The date passes, the reminder goes overdue, and the overdue pile grows. For a lot of people with ADHD, a growing pile of overdue items is not motivating; it is a reason to avoid opening the app at all. At that point the list has stopped working.</p>

<h2>Three changes that help</h2>
<ul>
  <li><strong>Only hard dates get hard dates.</strong> The dentist appointment on the 14th at 10:30 gets an exact date and a notification. "Book the dentist" does not.</li>
  <li><strong>Rough is fine.</strong> Give "book the dentist" a stretch of time instead: mid-October. In <a href="/">Remi</a> that is a <em>Mid October</em> reminder, visible for the whole 11th to 20th, not overdue on the 11th.</li>
  <li><strong>Maybes go somewhere else.</strong> Ideas and one-day projects go in <a href="/guides/someday-maybe-list-iphone/">Someday</a>, out of the way of what is actually next.</li>
</ul>
<figure>
  <img class="screen" src="/assets/guides/month.webp" alt="Remi month view for October 2026 with Pay rent, Book dentist check-up mid-October and Clean out the garage late October" loading="lazy" width="640" height="1284">
  <figcaption>Mid October and Late October sit alongside exact dates, without pretending to be them.</figcaption>
</figure>

<h2>Make it visible, make it quick</h2>
<ul>
  <li><strong>Visible:</strong> put a <a href="/guides/reminder-widget-iphone-home-screen/">widget</a> on your first Home Screen. A small Overdue counter is gentler than a full list.</li>
  <li><strong>Quick to capture:</strong> the faster a thought gets out of your head, the better. With Premium, press and hold + and say it: "clean out the garage late October".</li>
  <li><strong>Low pressure:</strong> no streaks to break, and approximate reminders do not go overdue on their first day. The rabbit does not judge. He literally can't.</li>
</ul>

<h2>When something truly cannot be missed</h2>
<p>Medication, a flight, a wake-up: those need something that rings through Silent, like an alarm, not a regular reminder. See the box below.</p>
""",
faqs=[
 ("What is a good reminder app for ADHD?", "One that does not force a date on everything, keeps the next task visible, and makes capturing a thought fast. Remi was built around approximate dates (early, mid, late in a month) and a Someday list, with Home Screen widgets and voice input."),
 ("Why do I ignore my reminders?", "Often because the list is full of overdue items that were never really due. Giving only real deadlines exact dates, and everything else a rough time or no date, keeps the list believable."),
],
xsell=XSELL_ALARM,
related=["reminder-without-date-iphone", "remind-me-sometime-next-month", "reminder-widget-iphone-home-screen"],
cta_h="Reminders without the guilt",
cta_p="Free on iPhone. No subscription, no account.",
),
# ---------------------------------------------------------------- 9
dict(
slug="plan-your-year-iphone",
cluster="see",
title="How to See a Whole Year of Reminders on iPhone",
meta="Renewals, birthdays, trips and seasonal chores on one screen. How to see a year of reminders at a glance on iPhone and spot busy months early.",
h1="How to See Your Whole Year of Reminders at a Glance",
lede="Most reminder apps show you today and maybe this week. The expensive surprises, the insurance renewal, the passport, the annual service, live further out than that.",
quick="""<strong>Quick answer:</strong> Use a year view that shows reminders, not just dates. <a href="/">Remi</a> has a <strong>Yearly</strong> tab that shows all twelve months with your reminder days marked and a count on each month, so you can see a crowded March coming in January.""",
body="""
<h2>Why a year view matters</h2>
<p>Lists are good at "what is next" and bad at "what is coming". A year laid out as twelve small calendars shows you shape: which months are crowded, which are quiet, where the renewals cluster. That is when you can do something about it, like moving the garage clear-out to a quiet month.</p>

<h2>The Yearly view in Remi</h2>
<ul>
  <li>All twelve months on one screen, scrolling on into next year.</li>
  <li>Each month shows a count of its reminders.</li>
  <li>Days with exact-date reminders are underlined; approximate reminders (Early, Mid, Late, Anytime) shade their stretch of the month.</li>
  <li>Tap a month to open it in the Month view.</li>
</ul>
<figure>
  <img class="screen" src="/assets/guides/yearly.webp" alt="Remi Yearly view of 2027 with every month shown and reminder days highlighted" loading="lazy" width="640" height="1284">
  <figcaption>A whole year on one screen. Busy months are obvious at a glance.</figcaption>
</figure>

<h2>Filling it in once</h2>
<p>Spend ten minutes adding the recurring things that come round every year: insurance and subscription renewals, the car and boiler services, birthdays, tax deadlines. Set them to repeat yearly and you will not need to do this again. See <a href="/guides/yearly-reminder-iphone/">yearly reminders</a> for how.</p>

<h2>Further than a year</h2>
<p>The free version covers the next twelve months. Premium lets you plan beyond that.</p>
""",
faqs=[
 ("Can I see all my reminders for the year on iPhone?", "Yes, in Remi. The Yearly tab shows all twelve months at once, with reminder days marked and a count on each month."),
],
related=["yearly-reminder-iphone", "remind-me-sometime-next-month", "reminder-widget-iphone-home-screen"],
cta_h="See the year before it happens to you",
cta_p="Free on iPhone. Planning beyond 12 months is part of Premium.",
),
# ---------------------------------------------------------------- 10
dict(
slug="voice-reminder-iphone",
cluster="see",
title="How to Add Reminders by Voice on iPhone (Even Vague Ones)",
meta="Say 'renew passport early November' and get exactly that. How to add reminders by voice on iPhone, including loose times and repeats.",
h1="How to Add Reminders by Voice on iPhone",
lede="The thought arrives while you are carrying shopping, or driving, or half asleep. If capturing it takes more than a few seconds, it is gone.",
quick="""<strong>Quick answer:</strong> Siri can add a reminder with a date and time. If you want to say something looser, like "early November" or "someday", <a href="/">Remi</a> Premium has its own voice input: press and hold the + button, say it, check it and save. It understands parts of the month, "next month", and repeats like "every 3 months".""",
body="""
<h2>How it works in Remi</h2>
<ol>
  <li>Press and hold the <strong>+</strong> button.</li>
  <li>Say the reminder the way you would say it to a person.</li>
  <li>Remi fills in the title, the time and any repeat. Check it and save.</li>
</ol>
<p>On iPhones that support it, speech recognition runs entirely on the device. Voice input is part of Premium.</p>

<h2>Things you can say</h2>
<ul>
  <li><em>"Renew passport early November"</em>: an Early November reminder.</li>
  <li><em>"Clean out the garage end of October"</em>: Late October.</li>
  <li><em>"Book the dentist next month"</em>: sometime next month.</li>
  <li><em>"Change the water filter every 3 months"</em>: a quarterly repeat.</li>
  <li><em>"Car insurance every year in March"</em>: yearly, in March.</li>
  <li><em>"Visit Lisbon"</em>: no date at all, so it goes into Someday.</li>
</ul>

<h2>Voice for the vague stuff</h2>
<p>Most voice assistants want a precise time, which is fine for "remind me at 6 to call Sam". The things that slip are the vague ones, and those are exactly what you can say to Remi without translating them into a fake date first.</p>
""",
faqs=[
 ("Can I add a reminder by voice without a specific date?", "Yes, in Remi. Press and hold the + button and say it. A reminder with no date becomes a Someday reminder, and phrases like \"early November\" or \"next month\" become approximate reminders."),
 ("Does Remi's voice input work on the device?", "On iPhones that support on-device speech recognition, yes: Remi asks for recognition to run on the device."),
],
related=["someday-maybe-list-iphone", "quarterly-reminder-iphone", "remind-me-sometime-next-month"],
cta_h="Say it the way you think it",
cta_p="Voice input is part of Premium: one $6.99 purchase, no subscription.",
),
# ---------------------------------------------------------------- 11
dict(
slug="reminder-vs-alarm-iphone",
cluster="repeat",
title="Reminder or Alarm? When an iPhone Reminder Isn't Enough",
meta="Most reminders are quiet on Silent and easy to swipe away; alarms ring. Since iOS 26.2 a reminder can ring too. Which to use for medication and wake-ups.",
h1="Reminder or Alarm? When an iPhone Reminder Isn't Enough",
lede="You set a reminder to take your tablet at 8. The phone was on Silent. It buzzed once, face down on the sofa, and that was that.",
quick="""<strong>Quick answer:</strong> A normal reminder is a notification: no sound on Silent, held back by Focus modes, easy to dismiss. An alarm rings until you stop it. Use reminders for things that can wait an hour. For the things that can't, use an alarm, or, on iOS 26.2 and later, mark the reminder <strong>Urgent</strong> in the built-in Reminders app, which makes it ring like an alarm.""",
body="""
<h2>What a normal reminder does</h2>
<p>A reminder in the built-in Reminders app, in Remi, or in any to-do app arrives as a notification. On iPhone that means:</p>
<ul>
  <li>One sound or buzz, at notification volume.</li>
  <li>No sound when the phone is on Silent, and held back by Focus modes unless you allow the app.</li>
  <li>Gone the moment you swipe it away.</li>
</ul>
<p>That is exactly right for most things: buy stamps, call the garage, pay rent this week. You see it when you look at your phone, and nothing breaks if that is an hour later.</p>

<h2>What an alarm does</h2>
<p>An alarm keeps ringing until you stop or snooze it, full screen, and it rings even with the phone on Silent or in a Focus. It is not something you can miss by having your phone face down.</p>

<h2>Urgent reminders (iOS 26.2 and later)</h2>
<p>Since iOS 26.2, the built-in Reminders app has an <strong>Urgent</strong> switch under Date &amp; Time. An Urgent reminder rings as an alarm at its due time, through Silent and Focus, with a fixed 9-minute snooze. If you only have one or two must-not-miss items and are on a recent iOS, that may be all you need. Remi's reminders do not have an alarm mode; they are always regular notifications.</p>

<h2>Which to use</h2>
<ul>
  <li><strong>Regular reminder:</strong> errands, chores, bills, renewals, birthdays, ideas, anything with a loose time. <a href="/">Remi</a> is built for these, including the ones with no exact date.</li>
  <li><strong>Urgent reminder or an alarm:</strong> waking up, medication, catching a flight, leaving for the school run, anything where "an hour later" is a problem.</li>
</ul>
<p>Plenty of people use both: Remi for the long list of things that need doing sometime, and an alarm for the few that need doing <em>now</em>.</p>
""",
faqs=[
 ("Do iPhone reminders make a sound on Silent?", "Normal reminders don't: they arrive as notifications, which make no sound on Silent and can be held back by Focus modes. Since iOS 26.2, a reminder marked Urgent in the built-in Reminders app rings as an alarm, including on Silent."),
 ("Should I use a reminder or an alarm for medication?", "If missing the time matters, use something that rings like an alarm: an alarm app, or an Urgent reminder in the built-in Reminders app on iOS 26.2 and later. Regular reminders are fine for things that can wait."),
 ("Can Remi reminders ring like an alarm?", "No. Remi's reminders are regular notifications. For alarms, use an alarm app or the built-in Reminders app's Urgent option."),
],
xsell=XSELL_ALARM,
related=["monthly-reminder-iphone", "adhd-reminder-app", "yearly-reminder-iphone"],
cta_h="For everything that can wait an hour",
cta_p="Free on iPhone. No account, no subscription.",
),
]

CLUSTERS = [
 ("nodate", "Reminders without a hard date",
  "Most reminder apps assume you know exactly when everything will happen. These guides are about the things you don't: ideas for one day, tasks for sometime next month, and how to keep them from either vanishing or going permanently overdue."),
 ("repeat", "Repeating reminders",
  "Rent every month, a filter every quarter, insurance every year. How to set repeats on iPhone, on a fixed date or for part of a month, and when a repeating reminder should really be an alarm."),
 ("see", "Seeing what's coming",
  "A reminder only works if you see it. Widgets for the Home Screen, a whole year at a glance, quick capture by voice, and a calmer setup for brains that hate fake deadlines."),
]

# Shown on /guides/ and as FAQPage structured data there. Kept true to the feature list above.
HUB_FAQS = [
 ("What is Remi?", "Remi is a reminder app for iPhone built around flexible dates: an exact date, a part of a month (early, mid or late), or no date at all. It is free, with a one-time Premium unlock."),
 ("Is Remi free?", "Yes. Remi is free to download and use, including exact, approximate and Someday reminders, the Today, Month and Yearly views, search, iCloud backup and two widgets. Premium is a single one-time purchase that adds repeating reminders, voice input, all eight widgets, planning beyond 12 months and more colours."),
 ("Is Premium a subscription?", "No. Premium is a one-time purchase. There is nothing to cancel."),
 ("Do I need an account?", "No. There is no sign-up. Your reminders are stored on your iPhone, with optional iCloud backup."),
 ("Does Remi work with the Calendar app?", "Remi can copy your reminders into the iPhone's calendar so they show up there. The sync is one-way, from Remi to the calendar."),
 ("Does Remi have Lock Screen widgets?", "No. Remi has eight Home Screen widgets."),
 ("Which iPhones does Remi run on?", "Any iPhone with iOS 17.6 or later."),
]
