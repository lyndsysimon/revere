=============================
 Revere: Streaming Event API 
=============================

Overview
========

Revere is intended to be used as a relay point, accepting inbound
notifications via HTTP and relaying them in JSON format to clients
via Websockets.

Requirements
============

Revere supports Python 3.3. Additional requirements may be be found in the
`requirements.txt`.

Client API
==========

Each event notification will contain the following elements:

+------------+---------------+------------------------------------+
| Element    | Type          | Content                            |
+============+===============+====================================+
| id         | String        | unique ID, alphanumeric,           |
|            |               | up to 32 characters                |
+------------+---------------+------------------------------------+
| category   | String        | The type of event; clients may use |
|            |               | this for specific handling actions |
+------------+---------------+------------------------------------+
| timestamp  | UTC Timestamp | when the event occured             |
+------------+---------------+------------------------------------+
| priority   | int; 0<=x<=5  | Relative importance, 5 being most  |
|            |               | important and 0 being              |
|            |               | informational only                 |
+------------+---------------+------------------------------------+
| text       | String        | The text to be displayed           |
+------------+---------------+------------------------------------+
