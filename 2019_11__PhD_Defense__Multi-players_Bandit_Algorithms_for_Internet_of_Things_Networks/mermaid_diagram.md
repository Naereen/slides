<!-- https://mermaidjs.github.io/mermaid-live-editor/ -->

sequenceDiagram
    participant D as IoT Device 🐄
    participant B as Base Station 📡
    Note left of D:Has data to send
    D->>B: Send uplink packet (Rx) on frequency F1
    Note right of B: Processing data…
    B->>D: Send downlink Ack. on F1
    rect rgb(18, 155, 0)
        D-->B: Successful transmission 😃 !
    end

sequenceDiagram
    participant D as IoT Device 🐄
    participant B as Base Station 📡
    Note left of D:Has data to send
    D-->>B: Collision on uplink packet (Rx)
    Note right of B: No received data!
    rect rgb(255, 100, 50)
        D-->B: Failed transmission 😭 !
    end