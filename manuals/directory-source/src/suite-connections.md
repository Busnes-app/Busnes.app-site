# Connect the Ky suite

Start with a working product, an everyday account and the [manual for that product](index.md).
Connect only the workflows you need. These instructions describe source reviewed on
November 17, 2026; use the product guides matching your installed revision for exact settings.

## Establish people and access first

1. Configure KyIdentity at a stable HTTPS origin and register each product's exact callback
   addresses. Assign the people who should use each application.
2. Configure the product's supported provisioning connector. Shared sign-in, directory
   provisioning and administrator grants are separate: verify all three. Keep administrator
   and everyday identities separate; use the everyday identity for mail, calendars, files and chat.
3. Set up suite groups in KyIdentity where supported. Participating apps reconcile a shared
   resource and its ordinary membership: Drive workspaces, Calendar calendars, Messages rooms
   and opt-in KyPost distribution lists. Product-specific permissions stay with each app;
   group membership grants no administrator role.
4. In KyIdentity's suite directory, configure the supported product pairs. Some products can
   instead use an explicit environment pair; follow their own guide. Keep the products on
   compatible versions and check their connection status. A launcher link alone enables no integration.
5. Use each product's documented private-network opt-in for LAN HTTPS endpoints when needed.
   Do not weaken HTTPS or copy a credential into a URL. Test one ordinary user's workflow before
   enabling it for everyone, then verify deactivation removes access in every receiving service.

Read [KyIdentity's setup manual](kyidentity-server/index.html) and its
[current suite-directory contract](https://github.com/Busnes-app/KyIdentity-server/blob/master/docs/SUITE-DIRECTORY.md).

## Send invitations and turn mail into work

Link KyPost and KyCalendar for the same KyIdentity identities. Enable the user's KyCalendar
connection in KyPost and test an invitation, a reply, an update and a cancellation. Native
KyPost mailboxes can send invitations too. Ordinary mailbox setup is separate from the pairing.
Native clients' supported RSVP behavior differs by release; check their own manual.

In the KyPost web interface, flagging a message can create a task in KyCalendar's Inbox list
with its subject, due date and a link back to the message. Completing the task clears the flag;
reopening it can set the flag again. The message body and attachments are not copied into the
task. A failed synchronization leaves the local mail flag in place and reports that the task
was not created; KyPost does not retry that send automatically. CalDAV task changes do not
send the completion callback.

KyCalendar also has task list, board and day views, planning and insights, public booking pages,
and administrator-managed rooms and equipment. These are implemented features, separate from
mail delivery and external CalDAV-client acceptance.

See [Calendar](kycalendar/index.html), [KyPost](kypost-server/index.html) and the
[mail/calendar contract](https://github.com/Busnes-app/KyPost-Server/blob/main/docs/KYCALENDAR.md).

## Add a meeting room or open a colleague's chat

Install the full KyMessages Matrix stack, including its media services for calls. Pair
KyCalendar with KyMessages and enable Video meeting in the event editor. The room follows the
meeting title and member list; cancelling the meeting closes the room. Members need the
corresponding app assignments and provisioned chat accounts. A healthy console alone does
not prove chat or calling works.

Meeting guests are a separate administrator opt-in in KyMessages, off by default. Their links
work only within the meeting windows; do not treat them as general guest access to the suite.
Test admission, expiration and cancellation. The optional meeting-notes bot sees the call's
plaintext when invited; text-message encryption does not establish call privacy or quality.

KyPost and KyCalendar can also open a colleague's chat when the user has the configured
KyMessages chat application. Read [KyMessages](kymessage-server/index.html) and the
[meeting-room and guest contract](https://github.com/Busnes-app/KyMessage-Server/blob/master/docs/KYCALENDAR.md).

## Share a Drive file without granting new access

KyIdentity provisions Drive staff; Drive owns file and workspace permissions. From KyPost or
KyCalendar, open the Drive picker and explicitly choose a file or link. An organisation link
still requires organisation access: an external attendee who can read the invitation cannot
therefore open the file. KyPost can instead attach a copy or use an explicitly created guest
link under Drive's sharing rules. A sent attachment is a separate copy that later Drive
revocation cannot recall.

Drive search covers names and supported document content, prefixes and exact phrases, with
access checked on each search. Its search index is rebuilt after restore. Desktop sync has
published packages; the separate Android client is pre-release and supports browsing and
transfers. Photo backup, persistent Android offline files and a document provider remain planned.

See [Drive Server](kydrive-server/index.html), [Desktop](kydrive-desktop/index.html),
[Android](kydrive-for-android/index.html) and the
[mail/Drive guide](https://github.com/Busnes-app/KyPost-Server/blob/main/docs/KYDRIVE.md).

## Share status and out-of-office dates

KyPost can send automatic out-of-office replies, with separate internal and external controls.
External replies require both administrator and user opt-ins; not every incoming message
qualifies for an automatic reply. An optional Calendar connection shows the absence there.

With the relevant pairs configured, KyCalendar sends busy intervals and KyPost sends
out-of-office dates to KyMessages, which answers colleague-status lookups. Titles, attendees,
locations and reply text are excluded from this status exchange. Sharing is on by default
for eligible members. In KyCalendar **Settings → Status**, turn off **Show my status to
colleagues** to clear those inputs and stop further sharing. Matrix last-active presence
remains disabled; Element does not show this suite status.

Read the [status contract](https://github.com/Busnes-app/KyMessage-Server/blob/master/docs/PRESENCE.md)
and [out-of-office rules](https://github.com/Busnes-app/KyPost-Server/blob/main/docs/OUT_OF_OFFICE.md).

## Receive alerts and watch certificate expiry

Configure KyPulse health sources and an off-host webhook receiver. Its Certificates page
tracks HTTPS leaf certificates from the health handshake and supports TLS-only targets.
Defaults are warning at 21 days and critical at seven; administrators can change them.
KyPulse reports expiry; it does not renew certificates.

For optional mail alerts, pair KyPulse with KyPost through KyIdentity. In KyPost, the mailbox
owner enables **Let KyPulse send alerts from my mailbox** and approves recipients; external
recipients confirm by link. Select that member and recipients in KyPulse and verify delivery.
Keep an independent off-host alert channel: mail can fail with the monitored service.

See [KyPulse](kypulse-server/index.html) and its
[monitoring guide](https://github.com/Busnes-app/KyPulse-server/blob/master/docs/MONITORING.md).

## Reserve work email before creating the SSO account

The generic HR JSON integration stages a source UID, asks KyPost to reserve a work address,
creates the KyIdentity account using the confirmed address, then writes it back to the HR
integration. It needs native KyPost mail, a configured source connector, HTTPS writeback and
separate application-access assignments. Configuration uses the administrator API; there is
no HR setup form. A mailbox reservation alone grants no app access. Vendor-specific Workday
adapters and tenant qualification are not included.

Use the [HR provisioning guide](https://github.com/Busnes-app/KyIdentity-server/blob/master/docs/HR-PROVISIONING.md)
for its supported requests, retry handling and offboarding contract.

## Choose placement and protect device connections

KyQuickStart AI is the guided installation path; KyQuickStart is its deterministic execution
layer and also runs unattended. Both use prepared infrastructure. In the installer catalog,
KyDrive, KyPost, KyDNS and KyMessages are Docker-only; Euro-Office is Kubernetes-only. The
other Ky servers support both targets, with a separate resident runner for KyYard.

KyIdentity can run PostgreSQL replicas on Kubernetes, optionally with a CloudNativePG database.
Other catalog Ky apps remain single-replica. This does not make a single-instance application
highly available. Read the [installer placement and limitations](https://github.com/Busnes-app/KyQuickStart/blob/master/docs/redirect.md).

Updated Drive clients sign requests with an enrolled device key and pin the server's TLS leaf.
Older links may need re-linking against a current server. For Drive and Post rollover, the
catalog NPM/nginx path copies only the served public certificate chain to the Docker host as
`KYDRIVE_TLS_CERT_FILE` or `KYPOST_TLS_CERT_FILE`; KyYard's handed-off suite runner refreshes
it daily and writes only on change. Keep the server's long-term identity key in backups.
An operator-owned API-only NPM has different limits. An explicitly enabled TLS probe is a
weaker trust mode, not a fallback. Follow the [TLS pin source guide](https://github.com/Busnes-app/KyQuickStart/blob/master/docs/edge.md).

KyAuth uses platform HTTPS trust rather than certificate pinning. Current QR pairing uses a
proof derived from the scanned token without transmitting the token; short-PIN pairing retains
trust-on-first-use limits. Current supported app sign-on binds the returned ID token to a
per-attempt proof key. Upgrade both sides for those guarantees; see [the security summary](../security.html).

## Prove the whole restore

Run the KyRecovery ceremony, protect the custodian cards, compare the pinned public-key ID,
and configure each product's destinations and schedule. KyRecovery stores sealed containers
it cannot decrypt; products restore outside it using their own commands and the custodian shares.

A full restore may also require Drive bulk snapshots, Messages media and Matrix recovery
keys, Notes encrypted blobs and user recovery material, plus deployment secrets. Calendar
capsules cover SQLite only; PostgreSQL requires an independently protected database backup
and deployment keys. Installer `backup`/`restore` covers Docker apps, not Kubernetes storage.
Native product restore tests and installer acceptance fixtures prove their stated paths,
not whole-suite production recovery. Restore disposable data and verify access and content
before depending on the backups.

Use [KyRecovery](kyrecovery-server/index.html) and each product's restore runbook. Keep
synchronization, same-host backup copies and independent off-host recovery separate.
