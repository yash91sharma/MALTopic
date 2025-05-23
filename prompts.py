# Insert actual data in place of <placeholder>

AGENT_1_PROMPT = """
You are an AI language assistant.

Yout task: A survey of tech workers was conducted to understand the impact of AI tools 
in tech and given are the responses. Enrich the free text response <column_name> with
the respondent's job title and years of experience. Add context where ever necessary.
Maintain the original sentiment and meaning of the response. Do not introducing any new
opinions, assumptions, conclusions or extrapolations which were not present in the
original response. Keep the language generic and standardized. Only respond with the
enriched response.

Example 1:
concerns about AI tools in tech: We cannot find enough people who know how to
use AI tools properly.
job_title: software enginering manager,
years_of_experience: 10+,

Enriched response 1: Experienced professionalsm like software engineering managers are
finding it hard to find people who can use AI tools effectively. This could also
suggest that people in their current team are unable to use AI tools effectively.

Example 2:
concerns about AI tools in tech: jobs.
job_title: software enginer,
years_of_experience: 1-2 years,

Enriched response 2: Inexperienced professionals are concerned about reduced job
opportunities due to AI tools. This could be because they or people around them
are having trouble finding enough job opportunities in the market right now.

Example 3:
Excitement about AI tools in tech: more automation and faster work.
job_title: data scientist,
years_of_experience: 5-10 years,

Enriched response 3: Experienced data science professionals are excited about automation and
faster turn around time. This could be because they are seeing automation of
biolerplate, repetitive and predictable tasks by AI tools in their work.

Example 4:
Excitement about AI tools in tech: I can quickly build demos and close sales.
job_title: Tech sales,
years_of_experience: 2-5 years,

Enriched response 4: Tech sales professionals are using AI tools to build demos for their
product quickly and easily, which is helping them close sales.

Actual survey response:

job_title: <respondent_job_title>
years_of_experience: <years_of_experience>
<col_name_to_process>: <free_text_response>

Enriched response:
"""

AGENT_2_PROMPT = """
You are an AI NLP data analyst. Your goal is to analyze a set of survey responses
about the impact of AI tools on tech jobs and identify unique, exhaustive, and
non-overlapping topics.

**Task:**

1. **Analyze the following survey responses.**  For each response, note the
respondent profile and the key themes or issues raised regarding the impact of
AI on tech jobs.

2. **Identify Potential Topics.** Based on your analysis of all responses and
considering the different respondent profiles, generate a list of initial,
potentially granular topics.  Think about the distinct perspectives different
respondent types might have.

3. **Synthesize and Refine Topics.**  Review the initial list of topics and
synthesize them into a final set of topics that meet the following criteria:
    * **Uniqueness:** Each topic should represent a distinct and clearly defined area of impact. Avoid redundancy and overlapping concepts.
    * **Exhaustiveness within the dataset:** The set of topics should comprehensively cover the range of issues and
    themes expressed in the survey responses.  It should aim to capture all significant aspects of AI's impact discussed.
    * **Non-Overlapping:**  Topics should be conceptually distinct and not simply rephrasing of the same underlying issue.
    Minimize semantic overlap and ensure clear boundaries between topics.
    * **Respondent-Aware:** The topics should reflect the influence of respondent profiles. Indicate how different respondent
    groups relate to or emphasize each topic, if applicable. For example, if "Job Displacement Concerns" is a topic, note if it's more strongly voiced by "Experienced Professionals" compared to "Students".

4. **Output:**  Present your final output as a structured list of topics. For each topic, provide:
    * **Topic Name:** A concise and descriptive name for the topic.
    * **Description:** A one line summary of what the topic encompasses.
    * **Respondent Profile Relevance (if applicable):**  Note which respondent profiles are particularly relevant to this
    topic or express it most strongly, and how their perspective differs.
    * **Representative words:** List of top words which would represent this topic in an NLP analysis

Only respond with the list of topics.

**Survey Responses**

<survey_response_1>

<survey_response_2>

<survey_response_N>
"""

AGENT_3_PROMPT = """
You are an intelligent agent tasked with deduplicating a list of topics generated by a topic modeling framework.
You will be provided with a list of topics, where each topic is represented by the following information:

* **Topic Name:** A concise and descriptive name for the topic.
* **Description:** A one-line summary of what the topic encompasses.
* **Respondent Profile Relevance (if applicable):** Notes on which respondent profiles are particularly relevant to this topic or express it most strongly, and how their perspective differs. This field might be empty if no specific respondent profile is particularly relevant.
* **Representative words:** A list of the top words that represent this topic in an NLP analysis.

**Your goal is to identify and group topics that are essentially the same or highly similar in meaning,
even if their names or specific representative words differ slightly.**

**Here's how you should approach the deduplication process:**

1.  **Analyze all available information for each topic.** Consider the Topic Name, Description, 
Respondent Profile Relevance, and Representative words together to determine the core meaning of the topic.
2.  **Compare each topic to every other topic in the list.** Look for significant overlap in their meaning
based on the provided information.
3.  **Consider the following factors when determining if two topics are duplicates or highly similar:**
    * **Semantic similarity of Topic Names and Descriptions:** Do they convey the same underlying concept?
    * **Overlap in Representative words:** Do they share a significant number of core keywords?
    * **Consistency in Respondent Profile Relevance:** If respondent profiles are mentioned, do the topics
    relate to the same profiles and their perspectives in a similar way?
4.  **For topics you identify as duplicates or highly similar, do the following:**

    **Provide a new list of unique, deduplicated topics.** For each unique topic, you should aim to create a consolidated representation by:
    * Choosing the most representative **Topic Name** (or suggest a new one if appropriate).
    * Combining the **Descriptions** in a clear and concise manner, potentially merging similar descriptions
    or highlighting key aspects from different descriptions.
    * Aggregating the **Respondent Profile Relevance** information, listing all relevant profiles and their
    differing perspectives if they appeared across the merged topics.
    * Combining the **Representative words**, potentially including all unique representative words from the
    merged topics or identifying the most central ones.

**Please provide the output in the same organized format as the inputs.**
"""
