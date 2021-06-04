# Graph Machine Learning

<a href="https://www.packtpub.com/product/graph-machine-learning/9781800204492"><img src="https://static.packt-cdn.com/products/9781800204492/cover/smaller" height="256px" align="right"></a>

This is the code repository for [Graph Machine Learning](https://www.packtpub.com/product/graph-machine-learning/9781800204492), published by Packt.

**Take graph data to the next level by applying machine learning techniques and algorithms**

## What is this book about?
Graph Machine Learning provides a new set of tools for processing network data and leveraging the power of the relation between entities that can be used for predictive, modeling, and analytics tasks.

This book covers the following exciting features: <First 5 What you'll learn points>
* Write Python scripts to extract features from graphs
* Distinguish between the main graph representation learning techniques
* Become well-versed with extracting data from social networks, financial transaction systems, and more
* Implement the main unsupervised and supervised graph embedding techniques
* Get to grips with shallow embedding methods, graph neural networks, graph regularization methods, and more


If you feel this book is for you, get your [copy](https://www.amazon.com/dp/180020390X) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>


## Instructions and Navigations
All of the code is organized into folders. For example, Chapter02.

The code will look like the following:
```
from stellargraph.mapper import HinSAGENodeGenerator
batch_size = 50
num_samples = [10, 5]
generator = HinSAGENodeGenerator(
 subgraph, batch_size, num_samples,
 head_node_type="document"
)
```
**Following is what you need for this book:**
This book is for data analysts, graph developers, graph analysts, and graph professionals who want to leverage the information embedded in the connections and relations between data points to boost their analysis and model performance. The book will also be useful for data scientists and machine learning developers who want to build ML-driven graph databases. A beginner-level understanding of graph databases and graph data is required. Intermediate-level working knowledge of Python programming and machine learning is also expected to make the most out of this book.

With the following software and hardware list you can run all code files present in the book (Chapter 1-14).

### Software and Hardware List

| Chapter  | Software required                   | OS required                        |
| -------- | ------------------------------------| -----------------------------------|
| 1 -10        | Python                    | Windows, Mac OS X, and Linux (Any) |
| 1 -10        | Neo4j            | Windows, Mac OS X, and Linux (Any) |
| 1 -10        | Gephi            | Windows, Mac OS X, and Linux (Any) |
| 1 -10        | Google colab or Jupyter notebook           | Windows, Mac OS X, and Linux (Any) |



We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](https://static.packt-cdn.com/downloads/9781800204492_ColorImages.pdf).

### Related products 
* Learn Grafana 7.0 [[Packt]](https://www.packtpub.com/product/learn-grafana-7-0/1838826580) [[Amazon]](https://www.amazon.com/dp/1788293770)

* Interactive Dashboards and Data Apps with Plotly and Dash [[Packt]](https://www.packtpub.com/product/interactive-dashboards-and-data-apps-with-plotly-and-dash/9781800568914) [[Amazon]](https://www.amazon.com/dp/1800568916)

## Get to Know the Authors
**Claudio Stamile**
received an M.Sc. degree in computer science from the University of Calabria (Cosenza, Italy) in September 2013 and, in September 2017, he received his joint Ph.D. from KU Leuven (Leuven, Belgium) and Université Claude Bernard Lyon 1 (Lyon, France). During his career, he has developed a solid background in artificial intelligence, graph theory, and machine learning, with a focus on the biomedical field. He is currently a senior data scientist in CGnal, a consulting firm fully committed to helping its top-tier clients implement data-driven strategies and build AI-powered solutions to promote efficiency and support new business models.

**Aldo Marzullo**
received an M.Sc. degree in computer science from the University of Calabria (Cosenza, Italy) in September 2016. During his studies, he developed a solid background in several areas, including algorithm design, graph theory, and machine learning. In January 2020, he received his joint Ph.D. from the University of Calabria and Université Claude Bernard Lyon 1 (Lyon, France), with a thesis entitled Deep Learning and Graph Theory for Brain Connectivity Analysis in Multiple Sclerosis. He is currently a postdoctoral researcher at the University of Calabria and collaborates with several international institutions.

**Enrico Deusebio**
is currently the chief operating officer at CGnal, a consulting firm that helps its top-tier clients implement data-driven strategies and build AI-powered solutions. He has been working with data and large-scale simulations using high-performance facilities and large-scale computing centers for over 10 years, both in an academic and industrial context. He has collaborated and worked with top-tier universities, such as the University of Cambridge, the University of Turin, and the Royal Institute of Technology (KTH) in Stockholm, where he obtained a Ph.D. in 2014. He also holds B.Sc. and M.Sc. degrees in aerospace engineering from Politecnico di Torino.
