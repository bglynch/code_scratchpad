# Abstract Base Classes(ABC) and Protocal

###### Top comment on [reddit thread discussion](https://www.reddit.com/r/Python/comments/1109kkx/python_interfaces_choose_protocols_over_abc/)

> Protocols and abstract classes are not interchangeable. You cannot simply choose one over the other. 
> There is a substantial difference: 
>
> - abstract class ensures that an implementation meets certain requirements when a subclass is declared,
> - protocol checks if an instance meets certain requirements when it's being used. 
> 
> They are different in the same way as "They are of the same kind" and "There are things that both of them can do".



## Abstract Base Class

> ### Basic Example
>
> ###### Create Abstract Base Class with expected methods(`@abstractmethod`)
>
> ```python
> # iot/device.py
> from abc import ABC, abstractmethod
> 
> from iot.message import MessageType
> 
> # Create abostact base class Device
> class Device(ABC):
>     @abstractmethod
>     def connect(self) -> None:
>         pass
> 
>     @abstractmethod
>     def disconnect(self) -> None:
>         pass
> 
>     @abstractmethod
>     def send_message(self, message_type: MessageType, data: str) -> None:
>         pass
> 
>     @abstractmethod
>     def status_update(self) -> str:
>         pass
> ```
>
> ###### Create classes that inherit from the ABC and implement the expected methods
>
> ```python
> # iot/devices.py
> from iot.device import Device
> from iot.message import MessageType
> 
> # Create multiple classes by inheriting from the base class Device
> class HueLight(Device):
>     def connect(self) -> None:
>         print("Connecting Hue light.")
> 
>     def disconnect(self) -> None:
>         print("Disconnecting Hue light.")
> 
>     def send_message(self, message_type: MessageType, data: str) -> None:
>         print(f"Hue light handling message of type {message_type.name} with data [{data}].")
> 
>     def status_update(self) -> str:
>         return "hue_light_status_ok"
> 
> 
> class SmartSpeaker(Device):
>     def connect(self) -> None:
>         print("Connecting to Smart Speaker.")
> 
>     def disconnect(self) -> None:
>         print("Disconnecting Smart Speaker.")
> 
>     def send_message(self, message_type: MessageType, data: str) -> None:
>         print(f"Smart Speaker handling message of type {message_type.name} with data [{data}].")
> 
>     def status_update(self) -> str:
>         return "smart_speaker_status_ok"
> 
> 
> class Curtains(Device):
>     def connect(self) -> None:
>         print("Connecting to Curtains.")
> 
>     def disconnect(self) -> None:
>         print("Disconnecting Curtains.")
> 
>     def send_message(self, message_type: MessageType, data: str) -> None:
>         print(f"Curtains handling message of type {message_type.name} with data [{data}].")
> 
>     def status_update(self) -> str:
>         return "curtains_status_ok"
> ```
>
> 



## Protocol (python >= 3.8)

- Dont inherit from a Protocal class
- Protocal defines the interface expected







---

Link

- [Protocol Or ABC In Python - When to use which one?](https://www.youtube.com/watch?v=xvb5hGLoK0A&ab_channel=ArjanCodes) : Arjan codes youtube video
  - [Githib repo](https://github.com/ArjanCodes/2021-protocol-vs-abc)