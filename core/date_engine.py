DATE_LIBRARY={
'Playful':[('Arcade + casual food','A shared game creates instant banter and removes pressure from constant conversation.','₹500–₹1,500'),('Bowling + dessert','Competitive enough to be fun without turning the date into an interview.','₹700–₹1,800'),('Mini golf + café','Easy movement, playful competition and natural pauses.','₹600–₹1,500'),('Board-game café','Structured activity with lots of room to talk.','₹500–₹1,300')],
'Romantic':[('Intimate dinner + walk','Choose somewhere comfortable to talk, then leave the evening open.','₹900–₹2,500'),('Café + scenic walk','A relaxed route works better than a rigid schedule.','₹400–₹1,200'),('Dessert + city lights','Short, flexible and easy to extend if the energy is good.','₹300–₹900'),('Dinner + live music','Good for atmosphere when the venue still allows conversation.','₹1,000–₹3,000')],
'Low-key':[('Quiet café + bookstore','Low pressure and easy to keep short or extend.','₹300–₹900'),('Coffee + slow walk','Simple enough that the date can breathe.','₹250–₹700'),('Dessert + people-watching','Leaves room for conversation to become the event.','₹250–₹650'),('Picnic + playlist swap','Personal without needing a large budget.','₹200–₹800')],
'Creative':[('Pottery workshop + coffee','A shared task creates conversation without forcing it.','₹800–₹2,000'),('Paint workshop + snack stop','Creative chaos creates memorable moments and jokes.','₹700–₹1,800'),('Art gallery + café','Strong when both people enjoy discussing ideas.','₹300–₹1,200'),('Bookstore challenge + dessert','Choose a book for each other in ten minutes.','₹300–₹1,000')],
'Foodie':[('Food crawl','Try several small stops instead of one long meal.','₹500–₹1,500'),('Coffee tasting + dessert','Shared discovery creates natural topics.','₹400–₹1,000'),('Street-food challenge','Pick three things neither person has tried.','₹300–₹900'),('Chef’s special dinner','Better for a deliberate sit-down evening.','₹1,000–₹3,000')],
'Adventurous':[('Escape room + food','A shared problem creates teamwork and banter.','₹700–₹2,000'),('Activity center + café','Movement gives the date a natural rhythm.','₹700–₹2,000'),('Day trip + local food','Best when you already know each other.','₹1,000–₹3,500'),('Outdoor activity + casual dinner','Balances movement and downtime.','₹800–₹2,500')],
'Conversation-heavy':[('Quiet café + walk','Prioritize venue quality and time to talk.','₹300–₹900'),('Bookstore + coffee','Topic changes happen naturally.','₹300–₹1,000'),('Museum + café','Shared observations create conversation.','₹300–₹1,200'),('Long lunch + short walk','Calmer structure when talking is the main point.','₹500–₹1,500')],
}
def build_plan(vibe,energy):
    ideas=list(DATE_LIBRARY.get(vibe,DATE_LIBRARY['Playful']))
    if energy<=3:
        q=[x for x in ideas if not any(w in x[0].lower() for w in ['bowling','arcade','escape','activity','mini golf'])]
        if q:ideas=q
    if energy>=8:
        a=[x for x in ideas if any(w in x[0].lower() for w in ['bowling','arcade','escape','activity','mini golf'])]
        if a:ideas=a+[x for x in ideas if x not in a]
    return ideas[:4]
