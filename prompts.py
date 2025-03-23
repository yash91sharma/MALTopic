# Insert actual data in place of <placeholder>

AGENT_1_PROMPT = """
You are an AI language assistant.

Yout task: A survey of tech workers was conducted to understand the impact of AI
tools in tech and given are the responses. Enrich the free text response with the
respondent's job title and years of experience. Add context where ever
necessary. Maintain the original sentiment and meaning of the response. Do not
introducing any new opinions, assumptions, conclusions or extrapolations which
were not present in the original response. Keep the language generic and
standardized. Only respond with the enriched response.

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
