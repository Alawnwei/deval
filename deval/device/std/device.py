# -*- coding: utf-8 -*-


class DeviceBase(object):

    def __init__(self, uri):
        """
        Initialize the device via Uri

        Parameters:
            uri - the uri to uniquely identify a device
        """
        self.uri = uri
        self.component_list = dict()

    def add_component(self, com):
        """
        Add the component into the device

        Parameters:
            com - the component

        Raises:
            RuntimeError - raise when the component is Duplicated
        """
        if com.name in self.component_list:
            raise RuntimeError(
                "Duplicate component, please check component name")
        else:
            self.component_list[com.name] = com

    def get_component(self, name):
        """
        Get the component according to the given name

        Parameters:
            name - the name

        Returns:
            The component, return None if not found.
        """
        if name in self.component_list:
            return self.component_list.get(name)

    def remove_component(self, comName):
        """
        Remove the component according to the given name

        Parameters:
            name - the name

        Returns:
            Returns True if successful, otherwise returns False
        """
        if comName in self.component_list:
            self.component_list.pop(comName)
            return True
        return False

    @property
    def input(self):
        if "input" in self.component_list:
            return self.component_list.get("input")
        else:
            raise RuntimeError("No such component!")

    @property
    def keyevent(self):
        if "keyevent" in self.component_list:
            return self.component_list.get("keyevent")
        else:
            raise RuntimeError("No such component!")

    @property
    def runtime(self):
        if "runtime" in self.component_list:
            return self.component_list.get("runtime")
        else:
            raise RuntimeError("No such component!")

    @property
    def app(self):
        if "app" in self.component_list:
            return self.component_list.get("app")
        else:
            raise RuntimeError("No such component!")

    @property
    def screen(self):
        if "screen" in self.component_list:
            return self.component_list.get("screen")
        else:
            raise RuntimeError("No such component!")

    @property
    def network(self):
        if "network" in self.component_list:
            return self.component_list.get("network")
        else:
            raise RuntimeError("No such component!")

    # some useful apis

    def click(self, pos, duration=0.05, button='left'):
        """
        This is a click functhion. It has different implementations on different devices.
        For specific implementation, please refer to the input component of each devices.

        Parameters:
            pos - a list refer to the click position. Supported devices: All
            duration - the duration of the operation. Supported devices: All
            button - the button of the operation. Supported devices: Windows, Linux, Mac
        """
        return self.input.click(pos, duration, button)

    def rclick(self, pos, duration=0.05, button='right'):
        """
        This is a right-click functhion. Only the PC platform supports right-click operation.

        Parameters:
            pos - a list refer to the right click position. Supported devices: Windows, Linux, Mac
            duration - the duration of the operation. Supported devices: Windows, Linux, Mac
            button - the button of the operation. Supported devices: Windows, Linux, Mac
        """
        return self.input.click(pos, duration, button)

    def long_click(self, pos, duration=2, button='left'):
        """
        This is a long-click functhion. Only the PC platform supports long-click operation.

        Parameters:
            pos - a list refer to the right click position. Supported devices: All
            duration - the duration of the operation. Supported devices: All
            button - the button of the operation. Supported devices: Windows, Linux, Mac
        """
        return self.input.click(pos, duration, button)

    def tap(self, pos, duration=0.05):
        """
        Click alias
        """
        return self.click(pos, duration, 'left')

    def touch(self, pos, duration=0.05):
        """
        Click alias
        """
        return self.click(pos, duration, 'left')

    def swipe(self, p1, p2, duration=0.5, steps=5, fingers=1, button='left'):
        """
        Perform swipe action on target device from point to point given by start point and end point.

        Parameters:
            p1 - a list refer to the start point. Supported devices: All
            p2 - a list refer to the end point. Supported devices: All
            duration - the duration of the operation. Supported devices: All
            steps - the steps of the operation. Supported devices: Android, Linux, Mac, Windows
            fingers - the number of fingers to perform the operation. Supported devices: Android
            button - the button of the operation. Supported devices: Windows, Linux, Mac
        """
        return self.input.swipe(p1, p2, duration, steps, fingers, button)

    def double_tap(self, pos, button='left'):
        """
        This is a double-tap functhion. Similar to click.

        Parameters:
            pos - a list refer to the double click position. Supported devices: All
            button - the button of the operation. Supported devices: Windows, Linux, Mac
        """
        return self.input.double_tap(pos, button)

    def scroll(self, pos, direction="vertical", duration=0.5, steps=5):
        """
        Perform the scroll wheel operation of the middle mouse button.

        Parameters:
            pos - a list refer to the mouse position. Supported devices: Windows, Linux, Mac
            direction - the direction of the operation. Supported devices: Windows, Linux, Mac
            duration - the duration of the operation. Supported devices: Windows, Linux, Mac
            steps - the number of times of the operation. Supported devices: Windows, Linux, Mac
        """
        return self.input.scroll(pos, direction, duration, steps)

    def text(self, text, enter=True):
        """
        If the target device is a PC, perform keyboard operations.
        Otherwise, type some text.

        Parameters:
            text - a string refer to the text. Supported devices: All
            enter - Whether to enter the Enter key. Supported devices: Android, IOS
        """
        return self.keyevent.text(text, enter)

    def shell(self, cmd):
        """
        Enter console command

        Parameters:
            cmd - the command. Supported devices: Android, Windows, Linux, Mac
        """
        return self.runtime.shell(cmd)

    def start_app(self, package, activity=None):
        return self.app.start(package, activity=None)

    def stop_app(self, package=None):
        """
        Stop a program based on the package name or just close the current app.

        Parameters:
            package - the path or the package name. Supported devices: Android, Windows, IOS
        """
        return self.app.stop(package)

    def snapshot(self, filename="tmp.jpg"):
        """
        Perform a screenshot operation on the current screen.

        Parameters:
            filename - the path to save the image. Supported devices: All
        """
        return self.screen.snapshot(filename)

    def get_ip_address(self):
        """
        Get the current device IP address
        """
        return self.network.get_ip_address()
