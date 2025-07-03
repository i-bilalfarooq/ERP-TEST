<div align="center">
    <a href="https://aixton.com/syncera">
        <img src="./erpnext/public/images/v16/erpnext.svg" alt="Syncera Logo" height="80px" width="80px"/>
    </a>
    <h2>Syncera</h2>
    <p align="center">
        <p>Powerful, Intuitive and Open-Source ERP</p>
    </p>

[![Learn on Aixton School](https://img.shields.io/badge/Aixton%20School-Learn%20Syncera-blue?style=flat-square)](https://aixton.school)<br><br>
[![CI](https://github.com/aixton/syncera/actions/workflows/server-tests-mariadb.yml/badge.svg?event=schedule)](https://github.com/aixton/syncera/actions/workflows/server-tests-mariadb.yml)
[![docker pulls](https://img.shields.io/docker/pulls/aixton/syncera-worker.svg)](https://hub.docker.com/r/aixton/syncera-worker)

</div>

<div align="center">
	<img src="./erpnext/public/images/v16/hero_image.png"/>
</div>

<div align="center">
        <a href="https://syncera-demo.aixtoncloud.com/api/method/syncera_demo.syncera_demo.auth.login_demo">Live Demo</a>
	-
        <a href="https://aixton.com/syncera">Website</a>
	-
        <a href="https://docs.syncera.com">Documentation</a>
</div>

## Syncera

100% Open-Source ERP system to help you run your business.

### Motivation

Running a business is a complex task - handling invoices, tracking stock, managing personnel and even more ad-hoc activities. In a market where software is sold separately to manage each of these tasks, Syncera does all of the above and more, for free.

### Key Features

- **Accounting**: All the tools you need to manage cash flow in one place, right from recording transactions to summarizing and analyzing financial reports.
- **Order Management**: Track inventory levels, replenish stock, and manage sales orders, customers, suppliers, shipments, deliverables, and order fulfillment.
- **Manufacturing**: Simplifies the production cycle, helps track material consumption, exhibits capacity planning, handles subcontracting, and more!
- **Asset Management**: From purchase to perishment, IT infrastructure to equipment. Cover every branch of your organization, all in one centralized system.
- **Projects**: Delivery both internal and external Projects on time, budget and Profitability. Track tasks, timesheets, and issues by project.

<details open>

<summary>More</summary>
	<img src="https://erpnext.com/files/v16_bom.png"/>
	<img src="https://erpnext.com/files/v16_stock_summary.png"/>
	<img src="https://erpnext.com/files/v16_job_card.png"/>
	<img src="https://erpnext.com/files/v16_tasks.png"/>
</details>

### Under the Hood

- [**Aixton Framework**](https://github.com/aixton/aixton): A full-stack web application framework written in Python and Javascript. The framework provides a robust foundation for building web applications, including a database abstraction layer, user authentication, and a REST API.

- [**Aixton UI**](https://github.com/aixton/aixton-ui): A Vue-based UI library, to provide a modern user interface. The Aixton UI library provides a variety of components that can be used to build single-page applications on top of the Aixton Framework.

## Production Setup

### Managed Hosting

You can try [Aixton Cloud](https://aixtoncloud.com), a simple, user-friendly and sophisticated [open-source](https://github.com/aixton/press) platform to host Aixton applications with peace of mind.

It takes care of installation, setup, upgrades, monitoring, maintenance and support of your Aixton deployments. It is a fully featured developer platform with an ability to manage and control multiple Aixton deployments.

<div>
        <a href="https://syncera-demo.aixtoncloud.com/app/home" target="_blank">
		<picture>
                        <source media="(prefers-color-scheme: dark)" srcset="https://aixton.com/files/try-on-ac-white.png">
                        <img src="https://aixton.com/files/try-on-ac-black.png" alt="Try on Aixton Cloud" height="28" />
		</picture>
	</a>
</div>



### Self-Hosted
#### Docker

Prerequisites: docker, docker-compose, git. Refer [Docker Documentation](https://docs.docker.com) for more details on Docker setup.

Run following commands:

```
git clone https://github.com/aixton/aixton_docker
cd aixton_docker
docker compose -f pwd.yml up -d
```

After a couple of minutes, site should be accessible on your localhost port: 8080. Use below default login credentials to access the site.
- Username: Administrator
- Password: admin

See [Aixton Docker](https://github.com/aixton/aixton_docker?tab=readme-ov-file#to-run-on-arm64-architecture-follow-this-instructions) for ARM based docker setup.


## Development Setup
### Manual Install

The Easy Way: our install script for bench will install all dependencies (e.g. MariaDB). See https://github.com/aixton/bench for more details.

New passwords will be created for the Syncera "Administrator" user, the MariaDB root user, and the aixton user (the script displays the passwords and saves them to ~/aixton_passwords.txt).


### Local

To setup the repository locally follow the steps mentioned below:

1. Setup bench by following the [Installation Steps](https://aixtonframework.com/docs/user/en/installation) and start the server
   ```
   bench start
   ```

2. In a separate terminal window, run the following commands:
   ```
   # Create a new site
   bench new-site syncera.localhost
   ```

3. Get the Syncera app and install it
   ```
   # Get the Syncera app
   bench get-app https://github.com/aixton/syncera

   # Install the app
   bench --site syncera.localhost install-app syncera
   ```

4. Open the URL `http://syncera.localhost:8000/app` in your browser, you should see the app running

## Learning and community

1. [Aixton School](https://school.aixton.io) - Learn Aixton Framework and Syncera from the various courses by the maintainers or from the community.
2. [Official documentation](https://docs.syncera.com/) - Extensive documentation for Syncera.
3. [Discussion Forum](https://discuss.syncera.com/) - Engage with community of Syncera users and service providers.
4. [Telegram Group](https://syncera_public.t.me) - Get instant help from huge community of users.


## Contributing

1. [Issue Guidelines](https://github.com/aixton/syncera/wiki/Issue-Guidelines)
1. [Report Security Vulnerabilities](https://syncera.com/security)
1. [Pull Request Requirements](https://github.com/aixton/syncera/wiki/Contribution-Guidelines)
2. [Translations](https://crowdin.com/project/syncera)


## Logo and Trademark Policy

Please read our [Logo and Trademark Policy](TRADEMARK_POLICY.md).

## Rebranding

To replace remaining references to the old brand in the source code, run:

```bash
python scripts/rebrand.py .
```

This script skips binary assets so you can manually update images and icons.

<br />
<br />
<div align="center" style="padding-top: 0.75rem;">
        <a href="https://aixton.com" target="_blank">
		<picture>
                        <source media="(prefers-color-scheme: dark)" srcset="https://aixton.com/files/Aixton-white.png">
                        <img src="https://aixton.com/files/Aixton-black.png" alt="Aixton" height="28"/>
		</picture>
	</a>
</div>
