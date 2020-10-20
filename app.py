from flask import Flask, render_template

app = Flask(__name__)

categories = {
    "art": {
        "books": [{
            "title": "The Meaning of Mariah Carey",
            "author": "by Mariah Carey (Goodreads Author), Michaela Angela Davis (Cowriter)",
            "description": "It took me a lifetime to have the courage and the clarity to write my memoir."
        }, {
            "title": "The Order",
            "author": "by Daniel Silva",
            "description": "From Daniel Silva, author of the # 1 New York Times bestsellers The New Girl and The Other Woman, comes a stunning new action-packed thriller of high stakes international intrigue featuring the enigmatic art restorer and master spy Gabriel Allon."
        }, {
            "title": "Nothing Ventured",
            "author": "by Jeffrey Archer",
            "description": "Nothing Ventured heralds the start of a brand new series in the style of Jeffrey Archer’s #1 New York Times bestselling Clifton Chronicles: introducing Detective William Warwick. But this is not a detective story, this is a story about the making of a detective . . ."
        }],
        "title": "Art",
        "subtitle": "Books that showcase particular types of art.",
        "route": "art",
    },
    "biography": {
        "books": [{
            "title": "Eat a Peach",
            "author": "by David Chang (Goodreads Author), Gabe Ulla",
            "description": "In 2004, David Chang opened a noodle restaurant named Momofuku in Manhattan's East Village, not expecting the business to survive its first year. In 2018, he was the owner and chef of his own restaurant empire, with 15 locations from New York to Australia, the star of his own hit Netflix show and podcast, was named one of the most influential people of the 21st century and had a following of over 1.2 million. In this inspiring, honest and heartfelt memoir, Chang shares the extraordinary story of his culinary coming-of-age."
        }, {
            "title": "Agent Sonya: Moscow's Most Daring Wartime Spy",
            "author": "by Ben Macintyre",
            "description": "The true story behind the Cold War’s most intrepid female spy."
        }, {
            "title": "A Knock at Midnight",
            "author": "by Brittany K. Barnett (Goodreads Author)",
            "description": "An inspiring true story about unwavering belief in humanity and an urgent call to free those buried alive by America's unjust legal system--from a gifted young lawyer whose journey marks the emergence of a powerful new voice in the movement to transform the system."
        }],
        "title": "Biography",
        "subtitle": "A biography (from the Greek words bios meaning 'life', and graphos meaning 'write') is a non-fictional account of a person's life. Biographies are written by an author who is not the subject/focus of the book.",
        "route": "biography",
    },
    "business": {
        "books": [{
            "title": "Mill Town: Reckoning with What Remains",
            "author": "by Kerri Arsenault (Goodreads Author)",
            "description": "A galvanizing and powerful debut, Mill Town is an American story, a human predicament, and a moral wake-up call that asks: what are we willing to tolerate and whose lives are we willing to sacrifice for our own survival?"
        }, {
            "title": "The Innovation Delusion: How Our Obsession with the New Has Disrupted the Work That Matters Most",
            "author": "by Lee Vinsel (Goodreads Author), Andrew L. Russell (Goodreads Author)",
            "description": "Innovation is the hottest buzzword in business. But what if its benefits has been exaggerated, and our obsession with finding the next big thing has distracted us from the work that matters most?"
        }, {
            "title": "How Today's Biggest Trends Will Collide and Reshape the Future of Everything",
            "author": "by Mauro F. Guillén",
            "description": "Bold, provocative...illuminates why we’re having fewer babies, the middle class is stagnating, unemployment is shifting, and new powers are rising."
        }],
        "title": "Business",
        "subtitle": "A business (also known as enterprise or firm) is an organization engaged in the trade of goods, services, or both to consumers. businesses are predominant in capitalist economies, where most of them are privately owned and administered to earn profit to increase the wealth of their owners. Businesses may also be not-for-profit or state-owned. A business owned by multiple individuals may be referred to as a company, although that term also has a more precise meaning.",
        "route": "business",
    },
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/category/<name>")
def category(name):
    return render_template("category.html", category=categories[name])


@app.route("/<category>/book/<int:id>")
def book(category, id):
    book = categories[category]['books'][id]
    return render_template("book.html", book=book)
