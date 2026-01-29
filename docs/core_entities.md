## Core Business Entities

### Customer
Represents an individual user interacting with the platform.

Attributes:
- customer_id
- signup_date
- geography
- acquisition_channel

### Transaction
Represents a completed purchase.

Attributes:
- transaction_id
- customer_id
- amount
- timestamp
- channel

### Campaign
Represents a marketing initiative.

Attributes:
- campaign_id
- start_date
- end_date
- budget
- channel

### Event
Represents user behavioral or system-generated events.

Attributes:
- event_id
- customer_id
- event_type
- timestamp
