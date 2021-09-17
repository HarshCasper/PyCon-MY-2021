+++
title = "PyCon Malaysia 2021: Building Polyglot applications using MetaCall Core"
outputs = ["Reveal"]
+++

# Building Polyglot applications using MetaCall Core
Harsh Mishra


{{< social >}}
{{< talk-link >}}


{{< figure src="images/metacall-logo.png" height="200px" >}}


---

# Agenda

- {{< frag c="Introduction to Polyglot development" >}}
- {{< frag c="Getting started with MetaCall Core" >}}
- {{< frag c="Understanding the underneath of the Core" >}}
- {{< frag c="Walking through a Polyglot Machine Learning application" >}}
- {{< frag c="Building a Polyglot application using Core" >}}
- {{< frag c="Q&A" >}}

---

# Problems at hand

<br><br>

- {{< frag c="Slow and painful migration of legacy codebases. Example: Java -> Node JS" >}}
- {{< frag c="Lack of interoperability between libraries across languages. Example: Python -> NodeJS" >}}
- {{< frag c="Embedding low level libraries or scripts in high-level environments." >}}

---

# Introduction to Polyglot development

{{< figure src="images/polyglot-development.png" height="500px" >}}

---

# Why Polyglot development?

<br><br>

- {{< frag c="Help developers find the best possible solution through any framework/library possible." >}}
- {{< frag c="Mix toolings, scripts, libraries amongst multiple languages without any friction." >}}
- {{< frag c="Embed low-level and high-level code without sacrificing any portability and interoperability." >}}

---

# What is MetaCall?

{{< figure src="images/metacall-logo.png" height="200px" >}}

MetaCall is an Open-Source Polyglot runtime.
It brings forward: 

- {{< frag c="Cross-language imports." >}}
- {{< frag c="Multiple language support through a CLI and runtime." >}}
- {{< frag c="N:N interoperability with a transparent API." >}}

---

# Demonstration

### sum.py
```py
def sum(a, b):
  return a + b
```

### main.js
```js
const { sum } = require('./sum.py');

sum(3, 4); // 7
```

### CLI

```sh
metacall main.js
```

---

# Installation

```sh{!|2|4|5|7|8}
# Installation using curl
curl -sL https://raw.githubusercontent.com/metacall/install/master/install.sh | sh

# Installation using wget
wget -O - https://raw.githubusercontent.com/metacall/install/master/install.sh | sh

# Installation using Docker
docker pull metacall/core
```

---

# Architecture of MetaCall

{{< figure src="images/metacall-architecture.png" height="500px" >}}

---

# Understanding Ports

<br><br>

- {{< frag c="Inner architecture of MetaCall Core is driven by ports." >}}
- {{< frag c="Ports offer MetaCall to other languages." >}}
- {{< frag c="C API wrappers expose the functions to other languages." >}}
- {{< frag c="Monkey Patching is used to make the API transparent for users overall." >}}

---

# Understanding Meta-Object protocol

{{< figure src="images/meta-object-protocol.png" height="500px" >}}

---

# Understanding Loaders

{{< figure src="images/metacall-loader.png" height="280px" >}}

- {{< frag c="Loaders are used for embedding languages into MetaCall." >}}
- {{< frag c="Act as plugins for a common interface wrapping the runtimes." >}}
- {{< frag c="Loading them dynamically during execution." >}}

---

# Introducting MetaCall FaaS

- {{< frag c="MetaCall FaaS allows us to deploy applications built on MetaCall Core" >}}
- {{< frag c="Provides automated API generation and high performance server over a Kubernetes cluster." >}}
- {{< frag c="Zero vendor locking and nudge towards NoOps development" >}}

---

# Benchmarks

{{< benchmarks >}}
{{< benchmark-code >}}

---

# Walking through a Polyglot Machine Learning application

{{< polyglot-machine-learning >}}
<br><br>
{{< figure src="images/metacall-ml.png" height="280px" >}}

---

# Building a Polyglot application

What are we going to do?

- {{< frag c="Write a simple Python script." >}}
- {{< frag c="Inspect the script using MetaCall CLI." >}}
- {{< frag c="Load a script module in an Express API." >}}
- {{< frag c="Test the API" >}}

---

# Thanks!

{{% grid middle %}}

{{< g 1 >}}
{{< figure src="images/metacall-logo.png" height="280px" >}}


{{< /g >}}

{{< g 1 >}}

Harsh Bardhan Mishra
{{< social >}}
{{< talk-link >}}

{{< /g >}}

{{% /grid %}}

---

# References

{{< references >}}
