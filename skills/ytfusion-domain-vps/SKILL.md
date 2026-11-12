---
name: ytfusion-domain-vps
description: Inspect, install, or migrate YtFusion dashboard and public domains on existing VPS deployments. Use for YouTube API Setup (/domain-setup), saved Server Transfer connections, DNS, HTTPS, and Google OAuth callbacks for those deployments.
---

# YtFusion Domain and VPS

Use the installed YtFusion workflow and respond in the user's language. Open
**YouTube API Setup** (`/domain-setup`) on the user's management device. If the
installation files are available, read `docs/setup/DOMAIN_CLOUDFLARE.md` from that
installation and check which actions its wizard actually offers.

## Identify the target and check its state

- Reuse the user's saved **Server Transfer** connection for the intended VPS.
  Match the target IP and the SSH account to that connection. Server Transfer
  uses its configured identity and port. Test with those settings before
  diagnosing a Server Transfer authentication failure.
- In **HTTPS VPS**, use the VPS status check. It can report an already working
  public dashboard without contacting the SSH helper. When SSH or helper access
  is the question, check the saved connection and the helper's status directly
  through the installed workflow. With shell access, inspect the installed
  Server Transfer configuration and use the same saved identity, verified host
  key, and read-only helper status operation. Keep key contents and passwords out
  of output, chat, and published files.
- Report DNS resolution, public HTTPS, and remote setup access separately. A
  certificate check on the VPS is evidence about the origin, while public
  readiness requires reaching the hostname from the management device. A request
  to inspect or discuss ends after the checks and explanation.

## Install or migrate when requested

1. Establish the desired primary domain, dashboard hostname, and whether the
   public homepage, privacy policy, and terms will also move. The wizard expects
   the dashboard hostname to be a subdomain of the primary domain entered. For
   a dashboard-only change, use the option to keep the existing public website
   when it already serves the selected primary domain.
2. Use the wizard's DNS records and apply the relevant changes in the user's DNS
   provider, normally Cloudflare. Verify the new hostname points to the target
   before starting HTTPS setup. Preserve unrelated DNS records. If a web login,
   second factor, or sudo password is required, let the user enter it directly
   in the appropriate UI.
3. Use **HTTPS VPS** to install through the matching Server Transfer connection.
   Activate or update the helper only when the installed workflow requires it.
   Confirm affected VPS jobs are idle before operations that can restart YtFusion.
   If the saved connection or remote helper is unavailable, follow the installed
   manual ZIP flow with authorized admin access. After a timeout, inspect VPS
   status before retrying because the remote installer may still be running.
4. For a migration with an overlap period, use **Add** (`Tambahkan`) so both
   hostnames can serve while the new one is tested. The wizard's replace action
   can retire a managed dashboard as soon as the origin passes its check, before
   browser or Google login verification. Retire the old hostname only when it
   is within the requested scope and the required checks have passed. The wizard
   protects the public website from this dashboard replacement action.
5. When the dashboard uses direct Google OAuth, register the exact new callback
   shown by the installed app. Reuse the configured Web client for a migration,
   or use the wizard's GCP step for a first setup. Keep the old callback during
   overlap and verify sign-in on the new HTTPS hostname. Update Google Branding
   links if the public site used there is moving. Verify the new dashboard and
   any moved public pages from the browser before reporting success.

Report which hostname was checked or changed, what was verified at the origin
and from the browser, and any step still pending. Scope changes to the requested
hostnames and integrations.
