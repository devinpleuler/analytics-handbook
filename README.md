## Soccer Analytics Handbook

[Devin Pleuler](https://twitter.com/devinpleuler) — April 2020

> This is probably overdue. I believe that people who have managed to wiggle themselves into dream jobs have a responsibility to help others reach there too. This was written during the depths of social isolation imposed by the COVID-19 pandemic. During this period, I've had an atypically large number of students and career changers reach out to me with questions, and a little extra free time, so I'm finally completing my assigned homework.
>
> There are plenty of resources out there that cover some of the more "*how do I get a job in sports analytics*" career-strategy questions out there, like [THIS](https://medium.com/@GregorydSam/getting-into-sports-analytics-ddf0e90c4cce) and [THIS](https://medium.com/@GregorydSam/getting-into-sports-analytics-2-0-129dfb87f5be) from [Sam Gregory](https://twitter.com/GregorydSam). This handbook is more geared at some of the technical skills, concepts, and sports analytics history that I think are worth familiarizing yourself with.
>
> In the handbook you can find three primary things:
1. Resources and suggestions for technical skills worth having for work in soccer analytics (but can probably be extended to other sports)
2. A series of tutorials delivered in `Jupyter` notebook format using `StatsBomb` Open Data, covering various data science techniques common in soccer analytics.
3. Collected research and articles that I believe are required reading to get up to speed with both the history and state-of-the-art in soccer analytics.
>
> Live long and prosper. 🖖🏻


---

##### Where to start?
The most important attributes for contributing to the soccer analytics landscape are a deep knowledge of the game, an ability to communicate clearly and effectively, and a bucket load of skepticism. Unfortunately, getting a job in soccer analytics is largely independent of these attributes and mostly depends on good fortune and timing. It is not a meritocracy, and I hope that changes.

But the most important *technical* skill once you have landed a job in soccer analytics is experience with scripting languages, preferably `Python` or `R` as they're great for data science.

I personally prefer `Python`, and therefore my recommendations will be geared in that direction. My primary reasons for this suggestion are:
- Simple syntax makes it great for first-time programmers
- Excellent documentation and community support
- Most analytics departments are using it
- Plays nicely with others
- [It's magic](https://xkcd.com/353/)

There are a ton of great resources online for learning `Python`, so I'm not going to reinvent the wheel here. Here are some that look good:
- [The Hitchhiker's Guide to Python](https://docs.python-guide.org/)
- [The Python Tutorial](https://docs.python.org/3/tutorial/index.html) direct from the official source: `docs.python.org`.
- *Plenty others*

Note: Starting with **Python 3** (I'd suggest version 3.7+) is probably the best route at this point. Python 2 is in the painful process of being put out to pasture.

---
##### Important Python Libraries
From a data science perspective, you can do *just about* anything worthwhile with the [`SciPy` Stack](https://www.scipy.org/stackspec.html). All of it's libraries are well-supported, and easily google-able if you run into issues. As a beginner, I wouldn't stray too far from these foundational libraries. If you do, you should have a decent reason for it. Some of its important components include:
- [`Numpy`](https://numpy.org/) - A fundamental library for scientific computing in `Python`. Particularly great for optimized vector and matrix calculations.
- [`Pandas`](https://pandas.pydata.org/) - A fast data analysis and manipulation library. It's `DataFrame` functionality is super useful (and reminiscent of some good bits of `R`)
- [`Matplotlib`](https://matplotlib.org/) is the de facto `Python` plotting library. It's finicky, but powerful. I've learned to love it.

I'd also suggest [`scikit-learn`](https://scikit-learn.org/stable/) (a.k.a. `sklearn`), which I find very user-friendly and is built on top of the libraries mentioned above. In our tutorials, we will predominantly use the `sklearn` implementations.

---
##### Where can I get data?

First, it's worth explaining what varieties of soccer performance data exist in the wild. Typically, and colloquially, there are two types of data: `Event Data` and `Tracking Data`.

**Event Data** is effectively chronological event-by-event tabulation of on-ball actions. It's typically collected from broadcast footage by third-party collectors and sold on the open market to clubs, broadcasters, the gambling industry, and even private individuals. The primary companies competing in this space are `Opta` (now owned by `STATS Perform`) and `StatsBomb`, but there are other competitors.

**Tracking Data** is an entirely different beast. Player tracking systems record the coordinate position of every player on the field (and usually the ball), many times per second. State-of-the-art systems collect up to 25 samples-per-second. Because these systems are expensive to install and operate, and require in-stadium hardware, this data is mostly available to the clubs themselves, but academics frequently get their hands on this data in a highly anonymized format through tediously painful research agreements. There are various competitors in this space, such as `ChyronHego`, `Second Spectrum`, `STATS Perform`, `Metrica`, `Signality`, and others.

The difference in scale between two data types is enormous. A single game of `Event Data` features around ~2-3 thousand individual events. A single game of `Tracking Data` represents 2+ million individual measurements.

**[StatsBomb](https://twitter.com/StatsBomb)** has provided a large volume of data **"freely available for public use"** via their [Open Data](https://github.com/statsbomb/open-data) repository on Github in order to better serve the analytics community. We will be using this data in some of the tutorials below.

Since the creation of this document, there has been some exciting developments in the world of publicly available data. **[Metrica](https://twitter.com/MetricaSports)** has released [two matches of tracking data](https://github.com/metrica-sports/sample-data), which are the first examples of publicly available tracking data to my knowledge. This is a huge contribution to the soccer analytics community, and I plan on contributing some examples of how to best use tracking data.

---
##### Jupyter Notebooks!
How could I go so long without mentioning [`Jupyter`](https://jupyter.org/)? That's because it deserves it's own section. I discovered Jupyter only a year-or-two ago, and I've become a much stronger analyst because of it.

`Jupyter` Notebooks are easily sharable documents that contain executable `Python` code alongside human-readable text for annotative purposes. They're perfect for sharing code and demonstrating concepts. We will be using these the deliver the tutorials below.

The notebooks will by hosted on [`Google Colab`](https://colab.research.google.com/), which allows you to write, run, and share `Jupyter` notebooks within your Google Drive. **For Free!**

If you're unfamiliar with `Google Colab` (or `Jupyter`), check out this **[introduction video](https://www.youtube.com/watch?v=inN8seMm7UI)**.

---
#### Soccer Analytics Tutorials

###### 1. Data Extraction & Transformation
> [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/devinpleuler/analytics-handbook/blob/master/notebooks/data_extraction_and_transformation.ipynb)
>
> Parsing raw `StatsBomb` data and storing it in a `Pandas` DataFrame

###### 2. Linear Regression
> [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/devinpleuler/analytics-handbook/blob/master/notebooks/linear_regression.ipynb)
>
> Examining the relationship between a player's pass volume and completion percentage

###### 3. Logistic Regression
> [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/devinpleuler/analytics-handbook/blob/master/notebooks/logistic_regression.ipynb)
>
> Predicting the outcome of a shot given its features

###### 4. Clustering
> [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/devinpleuler/analytics-handbook/blob/master/notebooks/clustering.ipynb)
>
> Identifying different types of passes

###### 5. Database Population & Querying
> [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/devinpleuler/analytics-handbook/blob/master/notebooks/database_population_and_querying.ipynb)
>
> Using `Pandas` & `SQLAlchemy` to store and retrieve `StatsBomb` event data

###### 7. Data Visualization
> [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/devinpleuler/analytics-handbook/blob/master/notebooks/data_visualization.ipynb)
>
> Create a Passing Network from the 2018 Men's World Cup Final

###### 8. Non-Negative Matrix Factorization
> [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/devinpleuler/analytics-handbook/blob/master/notebooks/non_neg_matrix_factorization.ipynb)
>
> Using `NNMF` to uncover spatial components of individual player contribution.

###### 9. Pitch Dominance
> [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/devinpleuler/analytics-handbook/blob/master/notebooks/pitch_dominance.ipynb)
>
> Loading and displaying the `Metrica` sample tracking data, and building a basic pitch dominance model.


###### 10. Convolutional Neural Networks
> [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/devinpleuler/analytics-handbook/blob/master/notebooks/nn_pass_difficulty.ipynb)
>
> Building pass difficulty surfaces using a convolutional neural network.


---
##### What other skills are worth picking up:
After the programming side, my suggestion is earning some experience with **relational databases**. In particular, I think [`MySQL`](https://www.mysql.com/) or [`PostgreSQL`](https://www.postgresql.org/) are great places to start. Like the rest of my recommendations, they're both open source. I mention that here because you can find a ton of enterprise solutions in this area.

Understanding `SQL`, which has various dialects (but you really only need to know one to adequately Google the quirks between them), is important for efficiently fetching data before processing it. At some clubs, for a hire that is coming into an already functioning analytics department, this skill is possibly the most important.

I use a lot of [`sqlalchemy`](https://www.sqlalchemy.org/), which has a little bit of a learning curve, but I've found tremendously useful for bridging the gap between `Python` and `SQL`. And it's super cross-platform.

Don't forget `Excel`. It's possibly the most important piece of software ever built. Nobody is _too good_ for Excel.

Having some **data-visualization** experience in your toolkit is also valuable. After `Matplotlib`, I would recommend:
- [`D3.js`](https://d3js.org/) is **highly recommended** for those with even a bit of `Javascript` and web development experience. The learning curve is totally worth it.
- [`Altair`](https://altair-viz.github.io/) for those making the transition over from `R` and really miss `ggplot`, one of `R` most redeeming qualities.
- [`Seaborn`](https://seaborn.pydata.org/) is a nice visualization library built on top of `Matplotlib`.
- [`Tableau`](https://www.tableau.com/) is totally fine. The tradeoff between customizability and ease of use is worth it in plenty of situations. Don't be a hero.
- Don't forget how powerful conditional formatting is in `Excel`.

Knowing some basic **version control** is really important for working effectively on a data science or analytics team. [`Git`](https://git-scm.com/) (and [GitHub](https://github.com/)) is the easy recommendation here. Also, **code testing** is a thing, unbeknownst to a majority of my code. I'd suggest using [`nose`](https://nose.readthedocs.io/en/latest/).

It's probably worth adding a note about **IDE**'s (*integrated development environment*) in here for the sake of completeness (i.e. what you write your code in). I've raved about `Jupyter` notebooks above, but they aren't great for larger software projects.

Personally, I enjoy using [`Atom`](https://atom.io/) (made by `GitHub`) because I'm apparently a glutton for punishment. A lot of people swear by [`PyCharm`](https://www.jetbrains.com/pycharm/), and others love [`VS Code`](https://code.visualstudio.com/). They're all fine. It's also smart to get familiar with `vim` or `emacs`, and general `bash` commands. Survival skills in the command-line environment is important when you start getting into data engineering stuff.

When you eventually reach a place where you might want to put some of your analytics stuff online, but don't want to leave `Python`, I'd suggest using one of these web frameworks:
- [`Flask`](https://flask.palletsprojects.com/en/1.1.x/) is an awesome lightweight framework that lets you prototype stuff easily and quickly. Great for building APIs.
- [`Django`](https://www.djangoproject.com/) is a fully-featured framework that is a bit harder to use, but does a lot of hard-stuff for you. It's ORM is quite similar to `sqlalchemy`, which is a plus.

And for the more-experienced analytics enthusiasts, I'd suggest picking up some of these:
- [`Apache Spark`](https://spark.apache.org/) (and [`Databricks`](https://databricks.com/)) for massive code parallelization across clusters.
- [`Numba`](http://numba.pydata.org/) for high performance Python.
- [`Tensorflow`](https://www.tensorflow.org/) and/or [`Keras`](https://keras.io/) for deep learning (also [`PyTorch`](https://pytorch.org/)).

There are lots of different ways to install both `Python` and all these different packages. The easiest way to get up and running on your local machine is probably [`Anaconda`](https://www.anaconda.com/). I also suggest learning how to use `pip` and [virtual environments](https://docs.python.org/3/tutorial/venv.html).

---
##### Soccer Analytics Research:

- **[A	 Framework	 for	 Tactical	 Analysis	 and	...](http://nessis.org/nessis11/rudd.pdf)** by [Sarah Rudd](https://twitter.com/srudd_ok)
- **[An Extension of the Pythagorean Expectation ...](https://www.soccermetrics.net/wp-content/uploads/2013/08/football-pythagorean-article.pdf)** by [Howard Hamilton](https://twitter.com/soccermetrics)
- **[Large-Scale Analysis of Soccer Matches ...](https://s3-us-west-1.amazonaws.com/disneyresearch/wp-content/uploads/20141211131038/Large-Scale-Analysis-of-Soccer-Matches-using-Spatiotemporal-Tracking-Data-Paper.pdf)** by Alina Bialkowski et. al
- **[Physics-Based	Modeling	of	Pass	Probabilities	in	Soccer](http://www.sloansportsconference.com/wp-content/uploads/2017/02/1621.pdf)** by [Will Spearman](https://twitter.com/the_spearman) et. al.
- **[Data-Driven	Ghosting	using	Deep	Imitation	Learning](http://www.sloansportsconference.com/wp-content/uploads/2017/02/1671-2.pdf)** by [Hoang	M. Le](https://twitter.com/HoangMinhLe),	Peter	Carr,	Yisong	Yue,	and	[Patrick	Lucey](https://twitter.com/patricklucey)
- **[Beyond Expected Goals](http://www.sloansportsconference.com/wp-content/uploads/2018/02/2002.pdf)** by [Spearman](https://twitter.com/the_spearman)
- **[Not All Passes Are Created Equal: ...](https://dl.acm.org/doi/pdf/10.1145/3097983.3098051)** by [Paul Power](https://twitter.com/counterattack9) et. all
- **[Wide Open Spaces: ...](http://www.sloansportsconference.com/wp-content/uploads/2018/03/1003.pdf)** by [Javier Fernandez](https://twitter.com/JaviOnData) and [Luke Bornn](https://twitter.com/LukeBornn)
- **[Decomposing	the	Immeasurable	Sport: ...](http://www.sloansportsconference.com/wp-content/uploads/2019/02/Decomposing-the-Immeasurable-Sport.pdf)** by [Fernandez](https://twitter.com/JaviOnData), [Bornn](https://twitter.com/LukeBornn), and [Dan Cervone](https://twitter.com/dcervone0)
- **[Modelling the Collective Movement of Football Players](http://uu.diva-portal.org/smash/get/diva2:1365788/FULLTEXT01.pdf)** by [Francisco José Peralta Alguacil](https://twitter.com/PeraltaFran23)
- **[Actions Speak Louder than Goals: ...](https://arxiv.org/pdf/1802.07127.pdf)** by [Tom Decroos](https://twitter.com/TomDecroos), [Lotte Bransen](https://twitter.com/LotteBransen), [Jan Van Haaren](https://twitter.com/JanVanHaaren), and [Jesse Davis](https://twitter.com/jessejdavis1)
> They've created a python library from this research. Find  in Resources section [below](#Resources).
- **[Dynamic Analysis of Team Strategy in Professional Footbal](https://static.capabiliaserver.com/frontend/clients/barca/wp_prod/wp-content/uploads/2020/01/56ce723e-barca-conference-paper-laurie-shaw.pdf)** by [Laurie Shaw](https://twitter.com/EightyFivePoint) and [Mark Glickman](https://twitter.com/glicko)
- **[Ready Player Run: Off-ball run identification and classification](https://static.capabiliaserver.com/frontend/clients/barca/wp_prod/wp-content/uploads/2020/01/40ba07f4-ready-player-run-barcelona.pdf)** by [Sam Gregory](https://twitter.com/GregorydSam)

---
##### Some Favorite Blog Posts
- **[Assessing	The	Performance	of Premier League Goalscorers](https://www.optasportspro.com/news-analysis/assessing-the-performance-of-premier-league-goalscorers/)** by [Sam Green](https://twitter.com/aSamGreen)
- **[Counting Across Borders](https://www.optasportspro.com/news-analysis/blog-counting-across-borders/)** by [Ben Torvaney](https://twitter.com/Torvaney)
- **[Defending Your Patch](https://deepxg.com/2016/02/07/defending-your-patch/)** by [Thom Lawrence](https://twitter.com/lemonwatcher)
- **[Pass Footedness in the Premier League](https://statsbomb.com/2019/04/pass-footedness-in-the-premier-league/)** by [James Yorke](https://twitter.com/jair1970)
- **[Messi Walks Better Than Most Players Run](https://fivethirtyeight.com/features/messi-walks-better-than-most-players-run/)** by [Bobby Gardiner](https://twitter.com/BobbyGardiner)
- **[Game of Throw-Ins](https://www.americansocceranalysis.com/home/2018/11/27/game-of-throw-ins)** by [Eliot McKinley](https://twitter.com/etmckinley)
- **[Expected Threat](https://karun.in/blog/expected-threat.html)** by [Karun Singh](https://twitter.com/karun1710)
- **[Passing Out at the Back](https://www.statsperform.com/resource/passing-out-at-the-back/)** by [Will Gürpinar-Morgan](https://twitter.com/WillTGM)
- **[The 10 Commandments of Football Analytics](https://theathletic.co.uk/1692489/2020/03/23/the-10-commandments-of-football-analytics/)** by [Tom Worville](https://twitter.com/Worville)
- **[Breaking Down Set Pieces ...](https://statsbomb.com/2019/05/breaking-down-set-pieces-picks-packs-stacks-and-more/)** by [Euan Dewar](https://twitter.com/EuanDewar)
- **[Data Based Coaching: ...](https://www.americansocceranalysis.com/home/2020/3/19/data-based-coaching-how-to-incorporate-data-driven-decisions-into-your-coaching-workflow)** by [Kieran Doyle](https://twitter.com/KierDoyle)
- **[Coaches Reward Goalscorers ...](https://www.americansocceranalysis.com/home/2020/3/30/coaches-reward-goalscorers-they-shouldnt)** by [McKinley](https://twitter.com/etmckinley) and [John Muller](https://twitter.com/johnspacemuller)

> Many of these are borrowed from [Sam Gregory](https://twitter.com/GregorydSam)'s list  [here](https://medium.com/@GregorydSam/best-football-analytics-pieces-e532844b12e). This is far from complete, and will definitely add to this from time to time.

---
##### Recommended Watching:

- [Self-Supervised Representations for Tracking Data](https://player.vimeo.com/video/398489039)
  > This 2020 OptaPro Forum talk from [Karun Singh](https://twitter.com/karun1710) represents some state-of-the-art research around autoencoders and feature extraction from tactical context.

- [An American Analyst in London](https://www.youtube.com/watch?v=LA9-V6_ZIUg)
  > Fun conversation at SSAC 2019 between StatsBomb CEO [Ted Knutson](https://twitter.com/mixedknuts), Houston Rockets GM [Daryl Morey](https://twitter.com/dmorey), and some other guy.

- [Beyond the Baseline: ...](https://www.youtube.com/watch?v=o9IjocHyBLE)
  >  This classic 2018 OptaPro Forum talk from the effervescent [Marek Kwiatkowski](https://twitter.com/statlurker) is one of my favorites. Suggests a mixed model approach for personalizing certain soccer metrics.

- [Some Things Aren't Shots](https://www.youtube.com/watch?v=5j-Ij5_3Cs8)
  > Great talk from [Thom Lawrence](https://twitter.com/lemonwatcher) at the 2019 StatsBomb Innovation Conference covering approaches to Expected Possession value.

- [Beyond Save Percentage](https://www.youtube.com/watch?v=V9_20e2ut14&t=1s)
  > Probably the smartest stuff I've seen on evaluation of goalkeeper performance, presented by [Derrick Yam](https://twitter.com/YAMiAM9).

- [Statistics for Hackers](https://www.youtube.com/watch?v=Iq9DzN6mvYA)
  > This PyCon 2016 talk from [Jake VanderPlas](https://twitter.com/jakevdp) is a great crash course in doing _statistics with for loops_. It really provides a great perspective for those of us without an extensive background in hard statistics. Great speaker, too.

---
##### Resources:

- [`socceraction`](https://github.com/ML-KULeuven/socceraction)
  > A python library for valuing the individual actions performed by soccer players. Includes an Expected Threat (xT) implementation. From [Tom Decroos](https://twitter.com/TomDecroos) et. al.

- [`statsbombpy`](https://github.com/statsbomb/statsbombpy)
  > A python library written by Francisco Goitia to access StatsBomb data.

- [`matplotsoccer`](https://github.com/TomDecroos/matplotsoccer)
  > A python library for visualising soccer event data. Also by [Tom Decroos](https://twitter.com/TomDecroos).

- [`ggsoccer`](https://github.com/Torvaney/ggsoccer)
  > Not `Python`, but this soccer visualization library from [Ben Torvaney](https://twitter.com/Torvaney) is great.

- [`statsbomb-data-parser`](https://github.com/imrankhan17/statsbomb-parser)
  > A python library to convert StatsBomb's JSON data into CSV format.

- [Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook)
  > [Jake VanderPlas](https://twitter.com/jakevdp) made his entire Python Data Science Handbook and accompanying Jupyter notebooks available online. It's a tremendous resource.

##### Books:
- [The Numbers Game](https://www.amazon.com/Numbers-Game-Everything-About-Soccer/dp/0143124560) by [Chris Anderson](https://twitter.com/soccerquant) and [David Sally](https://twitter.com/DavidSally6)
- [Football Hackers](https://www.amazon.com/Football-Hackers-Science-Data-Revolution-ebook/dp/B07NQM3YGK) by [Christoph Biermann](https://twitter.com/chbiermann)
- [Soccermatics](https://www.amazon.co.uk/Soccermatics-Mathematical-Adventures-Pro-Bloomsbury/dp/1472924142/ref=tmm_pap_swatch_0?_encoding=UTF8&qid=&sr=) by [David Sumpter](https://twitter.com/Soccermatics)

##### Looking for Ideas?
I maintain a [Twitter Thread](https://twitter.com/devinpleuler/status/1226917827304738818) of potential ideas that I think would be interesting soccer analytics projects.
