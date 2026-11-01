"""
Customer Support Agent with Coordinated Tools
Demonstrates strategic tool combination, error handling, and agent-as-tool pattern.

Reference: https://adk.dev/tools-custom/
"""

from google.adk.agents import LlmAgent

# Simulated database
ORDERS_DB = {
    "ORD123": {"status": "shipped", "total": 99.99, "customer": "john@email.com"},
    "ORD456": {"status": "processing", "total": 149.99, "customer": "jane@email.com"},
    "ORD789": {"status": "delivered", "total": 249.99, "customer": "bob@email.com"},
}


# Tool 1: Check order status
def check_order_status(order_id: str) -> dict:
    """Checks the current status of a customer's order.

    Use this when a customer asks about their order status or delivery.

    Args:
        order_id (str): The order ID (e.g., "ORD123").

    Returns:
        dict: Order status information.
            On success: {'status': 'success', 'order_status': '...', 'details': {...}}
            On error: {'status': 'error', 'error_type': 'not_found'/'invalid_format'}
    """
    # Validate format
    if not order_id.startswith("ORD"):
        return {
            "status": "error",
            "error_type": "invalid_format",
            "error_message": "Order IDs must start with 'ORD' (e.g., ORD123)"
        }

    # Look up order
    if order_id not in ORDERS_DB:
        return {
            "status": "error",
            "error_type": "not_found",
            "error_message": f"Order {order_id} not found in system"
        }

    # Success
    order = ORDERS_DB[order_id]
    return {
        "status": "success",
        "order_id": order_id,
        "order_status": order["status"],
        "details": order
    }


# Tool 2: Process refund
def process_refund(order_id: str, reason: str) -> dict:
    """Processes a refund request for an order.

    Use this ONLY after verifying the order exists with check_order_status.

    Args:
        order_id (str): The order ID to refund.
        reason (str): Customer's reason for refund.

    Returns:
        dict: Refund processing result.
            On success: {'status': 'success', 'refund_amount': X, 'reference': 'REF###'}
            On error: {'status': 'error', 'error_type': 'order_not_found'/'cannot_refund'}
    """
    # Check if order exists
    if order_id not in ORDERS_DB:
        return {
            "status": "error",
            "error_type": "order_not_found",
            "error_message": f"Cannot process refund - order {order_id} not found"
        }

    order = ORDERS_DB[order_id]

    # Check if order is eligible for refund
    if order["status"] == "delivered":
        # Simulate successful refund
        return {
            "status": "success",
            "refund_amount": order["total"],
            "reference": f"REF{order_id[3:]}",
            "estimated_days": 5,
            "message": "Refund processed successfully"
        }
    else:
        # Cannot refund orders not yet delivered
        return {
            "status": "error",
            "error_type": "cannot_refund",
            "error_message": f"Cannot refund order in '{order['status']}' status. Only delivered orders can be refunded."
        }


# Tool 3: Escalate to supervisor
def escalate_to_supervisor(issue_summary: str, order_id: str) -> dict:
    """Escalates complex issues to a human supervisor.

    Use this when you cannot resolve the customer's issue with available tools
    or when the customer explicitly requests to speak with a supervisor.

    Args:
        issue_summary (str): Brief summary of the issue (1-2 sentences).
        order_id (str): Related order ID if applicable.

    Returns:
        dict: Escalation confirmation.
            Always returns: {'status': 'success', 'ticket_id': 'TICKET###'}
    """
    # Generate ticket ID
    import random
    ticket_id = f"TICKET{random.randint(1000, 9999)}"

    return {
        "status": "success",
        "ticket_id": ticket_id,
        "message": "Issue escalated to supervisor",
        "estimated_response": "within 2 hours",
        "order_id": order_id if order_id else "N/A"
    }


# Create customer support agent with strategic instructions
root_agent = LlmAgent(
    model='gemini-3.5-flash',
    name="customer_support_agent",
    description="Handles customer inquiries about orders and refunds with comprehensive error handling.",
    instruction="""
    You are a helpful and empathetic customer support agent for an e-commerce company.

    # Your Capabilities

    You have three tools available:
    1. check_order_status(order_id) - Check the status of an order
    2. process_refund(order_id, reason) - Process refund requests
    3. escalate_to_supervisor(issue_summary, order_id) - Escalate complex issues

    # Workflow Guidelines

    ## For Order Status Inquiries:
    1. Greet the customer warmly
    2. Use check_order_status with the order ID they provide
    3. Handle the result:
       - If status='success': Provide clear status update with details
       - If error_type='not_found': Politely ask customer to verify the order ID
       - If error_type='invalid_format': Explain that order IDs start with "ORD" (example: ORD123)

    ## For Refund Requests:
    1. Express empathy for their situation
    2. FIRST use check_order_status to verify the order exists
    3. If order not found, cannot proceed with refund - ask customer to verify order ID
    4. If order exists, use process_refund with the order_id and customer's reason
    5. Handle refund result:
       - If status='success': Confirm the refund with reference number, amount, and timeframe
       - If error_type='cannot_refund': Explain why (order status) and offer alternatives or escalation
       - If error_type='order_not_found': This shouldn't happen if step 2 succeeded, but apologize and verify

    ## Error Handling Strategy:

    For 'not_found' errors:
    - Ask customer to double-check the order ID
    - Offer to search by email if they have it
    - Be patient and helpful

    For 'invalid_format' errors:
    - Politely explain the correct format: "ORD" followed by numbers
    - Provide an example: ORD123
    - Ask them to provide the order ID in correct format

    For 'cannot_refund' errors:
    - Explain the policy clearly (only delivered orders can be refunded)
    - Show empathy for their frustration
    - Offer to escalate to supervisor if they want an exception

    ## When to Escalate:
    Use escalate_to_supervisor when:
    - Customer is frustrated or angry and requests supervisor
    - Issue cannot be resolved with available tools
    - Customer requests policy exception
    - Multiple tool attempts have failed
    - Customer specifically asks to speak with a manager

    After escalating:
    - Provide the ticket ID
    - Tell them expected response time
    - Thank them for their patience

    # Communication Style
    - Always be polite, professional, and empathetic
    - Use the customer's name if you know it
    - Provide clear next steps
    - Acknowledge their feelings (frustration, concern)
    - Thank them for their patience
    - Never make promises you can't keep
    """,
    tools=[check_order_status, process_refund, escalate_to_supervisor]
)
