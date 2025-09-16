# Brainstorming RAG Data

By now, you should have a clearer picture of what RAG is. Tomorrow, you’ll start building your own RAG application. To do that, you’ll need something to retrieve. This document is meant to spark ideas about possible data sources and help you evaluate which ones make sense.

### What makes a good RAG data source?

For a data source to be suitable for RAG, it should be:

1. **Plentiful**. If your data source is only a few pages of content, then you could just put the whole thing in the context window and move on. You don't need to chunk it at all. You don't need to have thousands of pages, but aim for something large enough that you would hesitate to throw all of it into a prompt.

2. **Exclusive**. Your source should contain information that isn’t already widely known or easily handled by a base model. Wikipedia, for example, isn’t ideal—models already know that content.

3. **Domain-specific**. The more your data covers a particular topic area, the more value RAG adds. Generic, widely known data doesn’t give you much of an edge since the model already has general knowledge.

Here's a short list of some of the **best** RAG data sources:

- **Internal Documents.** The gold standard. These are highly valuable because they’re unique to you or a company and completely unknown to general models.
- **Policies, Procedures, and Regulations.** Highly specific, frequently updated, and too detailed to memorize. Perfect for customer service or compliance tools.
- **Knowledge Bases and FAQs.** Structured around common questions, which makes them especially retrieval-friendly. (For example, the Launch School curriculum powers LSBot.)
- **Research Papers or Reports.** Dense and niche. Ideal for academic or specialized use cases.
- **Product or API Documentation.** Long, technical, and constantly referenced by developers or support teams.
- **Transcripts (Meetings, Calls, Interviews).** Raw at first, but once chunked, they capture unique details that aren’t stored anywhere else.

> When considering a source, ask: _Would a general-purpose model already know this? Or would retrieval actually add value here?_

### Choose Your Data

If you don’t have your own data, take inspiration from these datasets or explore Kaggle and HuggingFace for more options.

- [A dataset of wine reviews](https://www.kaggle.com/datasets/zynicide/wine-reviews/data)
- [A huge collection of historical newspapers from the U.S.](https://huggingface.co/datasets/dell-research-harvard/AmericanStories)
- [ASRS (Aviation Safety Reporting System) incident reports](https://huggingface.co/datasets/elihoole/asrs-aviation-reports/viewer/default/train?views%5B%5D=train&row=7)
- [Old Bailey Proceedings 1740-1913 (old court cases)](https://www.digitalpanopticon.org/Old_Bailey_Proceedings_1740-1913)

...and tons of other topics! If you have an area you’re interested in, look for a dataset that fits.

You don’t need to lock in your data source today, but having a few ideas ready will let you spend more time building something cool.