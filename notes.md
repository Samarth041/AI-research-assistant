# Lesson: `client.py`

## 1. `__init__()` Method

The `__init__()` method initializes the objects that the client will need throughout its lifetime.

### Initialize the following:

- **`server_params`**
  - Stores the server configuration (command, arguments, environment variables, etc.).
  - Used later to start the MCP server.

- **`session`**
  - Initially set to `None`.
  - Will later hold the `ClientSession` object after connecting to the server.

- **`AsyncExitStack`**
  - Used to manage multiple asynchronous resources.
  - Automatically cleans up resources (transport, session, etc.) when the client exits or an error occurs.

---

## 2. `connect()` Method

The `connect()` method establishes the connection with the MCP server.

### Step 1: Create the transport

Use the stored `server_params` to create a **stdio transport**.

This creates two communication streams:

- **Read stream (`read`)**
  - Receives messages from the server.

- **Write stream (`write`)**
  - Sends messages to the server.

---

### Step 2: Create the `ClientSession`

Pass the `read` and `write` streams to create a `ClientSession`.

The session represents the active communication channel between the client and the MCP server.

---

### Step 3: Initialize the session

Call the session's initialization method.

This performs the MCP handshake, allowing the client and server to exchange capabilities and prepare for communication.

---

## Flow

```text
Client
   │
   ▼
__init__()
   │
   ├── Store server_params
   ├── session = None
   └── Create AsyncExitStack
   │
   ▼
connect()
   │
   ├── Create stdio transport
   │      ├── read
   │      └── write
   │
   ├── Create ClientSession(read, write)
   │
   └── Initialize session
```
----