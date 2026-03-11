from langchain_core.tools import tool
from rag.retriever import get_retriever
from datetime import datetime


# -----------------------------
# 1. Hospital Knowledge Tool (RAG)
# -----------------------------
@tool
def hospital_knowledge_tool(query: str) -> str:
    """
    Use this tool when the user asks about hospitalisation information such as:
    - admission documents
    - surgery preparation
    - hospital discharge
    - follow-up care
    """

    categories = [
        "ADMISSION_DOCS",
        "PREPARATION_DOCS",
        "DISCHARGE_DOCS",
        "FOLLOWUP_DOCS"
    ]

    results = []

    for category in categories:
        retriever = get_retriever(category)

        if retriever:
            docs = retriever.invoke(query)
            results.extend(docs)

    if not results:
        return "No relevant hospital information found."

    context = "\n\n".join([doc.page_content for doc in results[:4]])

    return f"""
Relevant hospital information:

{context}
"""


# -----------------------------
# 2. Contact Representative Tool
# -----------------------------
@tool
def contact_representative_tool(query: str) -> str:
    """
    Use this tool when the user wants to talk to a hospital representative
    or needs human assistance.
    """

    return """
Hospital Support Contact

You can contact a hospital representative using the following options:

Phone: +91-1234567890
Email: support@hospitalhelp.com
Help Desk: Available 24/7 at the hospital reception

A representative will assist you with admission, billing, and medical queries.
"""


# -----------------------------
# 3. Surgery Details Tool (Dummy Dataset)
# -----------------------------
@tool
def surgery_details_tool(patient_id: str) -> str:
    """
    Use this tool when the user asks about:
    - surgery date
    - surgery time
    - operation schedule
    - surgery report
    """

    dummy_database = {
        "P1001": {
            "name": "Rahul Sharma",
            "surgery": "Appendix Removal",
            "date": "15 March 2026",
            "time": "10:30 AM",
            "doctor": "Dr. Mehta",
            "status": "Scheduled"
        },
        "P1002": {
            "name": "Anita Verma",
            "surgery": "Knee Replacement",
            "date": "18 March 2026",
            "time": "02:00 PM",
            "doctor": "Dr. Patel",
            "status": "Confirmed"
        }
    }

    patient = dummy_database.get(patient_id)

    if not patient:
        return "Patient record not found."

    return f"""
Patient Surgery Details

Name: {patient['name']}
Surgery: {patient['surgery']}
Date: {patient['date']}
Time: {patient['time']}
Doctor: {patient['doctor']}
Status: {patient['status']}
"""


# -----------------------------
# Tool list used by the agent
# -----------------------------
TOOLS = [
    hospital_knowledge_tool,
    contact_representative_tool,
    surgery_details_tool
]