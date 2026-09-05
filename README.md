<!-- ============================ HEADER ============================ -->

<p align="center">
  <img src="https://raw.githubusercontent.com/lieutenant-Rohit/lieutenant-Rohit/main/terminal-header.svg" alt="animated terminal header"/>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/rohit-bisht-078642379/">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/>
  </a>
  <a href="mailto:rohitbishtt69@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white"/>
  </a>
  <a href="https://leetcode.com/u/rohit316/">
    <img src="https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=black"/>
  </a>
</p>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:3FB950,100:6BAA75&height=2&section=header" width="100%"/>

## <code>rohit@dev:~$</code> 🧭 About Me

- 🎓 Final-year **MCA** student at **Uttaranchal University**, Dehradun — Class of 2027
- 🛠️ Backend-focused engineer with strong **Java / Spring Boot** foundations
- 🔍 Currently building **MeshPay** — an offline, mesh-routed UPI payment relay
- 📈 **767+ LeetCode problems solved** — ranked **top 4% globally**
- 🚀 Actively interviewing for **SDE Internship** roles
- 💬 Ask me about Spring Security, JWT auth, JPA/Hibernate, or system design

<details>
<summary>💡 Or in Java, if you'd prefer</summary>

```java
@Component
public class Rohit implements BackendDeveloper {

    private final String role        = "Java / Spring Boot Developer";
    private final String education   = "MCA, Uttaranchal University (2025–2027)";
    private final boolean openToWork  = true;

    private final String[] stack = {
        "Java 21", "Spring Boot 3", "Spring Security", "JPA / Hibernate",
        "PostgreSQL", "Redis"
    };

    @Override
    public String currentFocus() {
        return "MeshPay — UPI without internet";
    }

    public static void main(String[] args) {
        System.out.println(new Rohit().currentFocus());
    }
}
```

</details>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:6BAA75,100:7AA2F7&height=2&section=header" width="100%"/>

## <code>rohit@dev:~$</code> ⚡ Tech Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=java,spring,python,postgres,mysql,redis,maven,git,github,docker,linux,postman,nginx&perline=7"/>
</p>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:6BAA75,100:7AA2F7&height=2&section=header" width="100%"/>

## <code>rohit@dev:~$</code> 🔬 Flagship Project — MeshPay

Offline UPI payment prototype that routes transactions across a 10-node phone mesh without internet — combining GPSR routing, X25519/Ed25519 encryption, and a Spring Boot bank backend.

| Signal | Method |
|---|---|
| Mesh Routing | GPSR (Greedy Perimeter Stateless Routing) |
| Encryption | X25519 key exchange + Ed25519 signatures |
| Backend | Spring Boot REST API |
| Simulation | 10-node phone mesh network |

`Java 21` `Spring Boot` `Python` `Docker` `Cryptography`

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:6BAA75,100:7AA2F7&height=2&section=header" width="100%"/>

## <code>rohit@dev:~$</code> 🚀 Other Projects

<table>
<tr>
<td width="33%" valign="top">

### 🌸 [BloomsCafe](https://github.com/lieutenant-Rohit/BloomsCafe)
Full-stack cafe e-commerce platform with JWT authentication, Redis caching, and PostgreSQL primary-replica read/write splitting. Load tested to 700 concurrent users with 0% errors.

`Java 21` `Spring Boot` `PostgreSQL` `Redis`

</td>
<td width="33%" valign="top">

### 🦖 [Rex](https://github.com/lieutenant-Rohit/rex)
A Git-like version control system built from scratch — content-addressable object storage, tree snapshots, and branching, no VCS libraries.

`Java 21` `SHA-1` `zlib`

</td>
<td width="33%" valign="top">

### 🔧 More Coming Soon...
Building distributed systems, system design patterns, and open source tools.

`Distributed Systems` `System Design`

</td>
</tr>
</table>

<details>
<summary>🔍 Rex object model (blob → tree → commit)</summary>

```
  working dir           .rex/objects/
  ┌──────────┐          ┌─────────────────────┐
  │ a.txt    │  hash    │ 3a17...  [blob]      │
  │ b.txt    │ ───────► │ 9f02...  [blob]      │
  └──────────┘          │ c451...  [tree]  ────┼─┐
                         │ 88de...  [commit]────┼─┼─► points to tree + parent
                         └─────────────────────┘ │
                                    ▲             │
                                    └─────────────┘
  Every object is content-addressed by SHA-1 and zlib-compressed —
  identical content always produces the identical hash, so Rex never
  stores the same blob twice.
```

</details>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:6BAA75,100:7AA2F7&height=2&section=header" width="100%"/>

## <code>rohit@dev:~$</code> 📊 GitHub Statistics

<p align="center">
  <img height="165" src="https://github-readme-stats.shion.dev/api?username=lieutenant-Rohit&show_icons=true&theme=tokyonight&hide_border=true&count_private=true"/>
  <img height="165" src="https://github-readme-stats.shion.dev/api/top-langs/?username=lieutenant-Rohit&layout=compact&theme=tokyonight&hide_border=true"/>
</p>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:6BAA75,100:7AA2F7&height=2&section=header" width="100%"/>

## <code>rohit@dev:~$</code> 💻 LeetCode

Live stats below, refreshed automatically once a day by a GitHub Action (`.github/workflows/update-readme.yml`) — no third-party badge service, just a script pulling straight from LeetCode's own API.

<!--LEETCODE:START-->
```text
$ leetcode --profile rohit316
Solved     : 767 problems
  Easy     : —
  Medium   : —
  Hard     : —
Global rank: —
Updated    : not yet run — first Action run will populate this
```
<!--LEETCODE:END-->

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:6BAA75,100:7AA2F7&height=2&section=header" width="100%"/>

<p align="center">
  <i>"Programs must be written for people to read, and only incidentally for machines to execute."</i><br/>
  <b>— Harold Abelson</b>
</p>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:7AA2F7,100:6BAA75&height=120&section=footer"/>