# Water Bottle CTF

This room focused on practicing OSINT (Open Source Intelligence) techniques.

## Scenario

We were told that someone had recently moved back to their home area after being away since 2014. They remembered a water refilling station located off Boni Avenue, but it had since been replaced by a newer station sometime after 2014.

The objective was to identify:

* The name of the old water refilling station
* Its phone number

The challenge also provided the clue that the first five digits of the number were:

```text
63922
```

---

## Initial Research

I started by researching **Boni Avenue**, which is a well-known area in **Manila, Philippines**.

Next, I investigated countries that commonly use 12-digit phone numbers beginning with `63`. One of the first results was the **Philippines**, which uses the international country code:

```text
+63
```

This matched the clue provided in the room, confirming that the target location was likely somewhere around Boni Avenue in the Philippines.

---

## Google Maps Investigation

I then moved to **Google Maps** and searched for:

```text
Boni Ave Water Station
```

From there, I manually reviewed various water refilling stations and compared their current listings against historical Street View imagery from around 2014.

One location stood out:

* Current business: **Alkafresco Water Refilling Station**
* 2014 Street View business: **Aquabest**

I initially tried using:

```text
THM{aquabest_639225316570}
```

but that was incorrect.

---

## Expanding the Search

At this point, I searched Google for:

```text
Aquabest Mandaluyong
```

This led me to a contact listing page containing additional information for the business.

The listing included the phone number:

```text
63 922 872 1228
```

Using the room’s expected flag format, I submitted:

```text
THM{aquabest_639228721228}
```

Success.

---

# Takeaways

* Basic OSINT techniques can be extremely effective.
* Google Maps and historical Street View data are valuable tools for investigating older business information.
* Small clues like phone prefixes and location names can quickly narrow down a search area.
* Combining multiple open-source tools often leads to the answer faster than relying on a single source.
