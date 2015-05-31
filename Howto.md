First, the person giving support needs to:

  1. Launch Gitso.
  1. Click on "Give Support"
  1. Click "Start"

Second, the person who needs help, needs to:

  1. Launch Gitso.
  1. Click on "Get Help"
  1. Type in the "IP Address" provided by the supporter
  1. Click "Start"

Now the person who needs help sits back and watches as someone else moves their mouse and operates their pc from afar.

Note: The person who is giving support needs to have port 5500 open to their machine which requires a port forward on a NATed network.

## FAQ ##
  * **Q:** I want to help someone, but I’m behind a router, and it doesn’t work!
  * **A:** The person who is going to “give support” must have port 5500 open to their PC. This usually means enabling port forwarding on your router and poking holes through any firewalls.

  * **Q:** How do I get an IP that can be reached by a person who is in another city or simply another ISP(network)? I don't have an IP. The public IP that I get from a whatismyip type website is actually common to everybody around me.
  * **A:** In order to give support through Gitso, you need to be able to have access to the firewall/router of the subnet you're on. If you don't have access to that, you unfortunately won't be able to use Gitso. If you do have access, then you forward the external IP/port to your internal IP/port. Usually in VNC, it's the person "getting support" who has to do this, but with Gitso, we reverse this and have the person "giving support" set this up. For example, that's what I do at home. But when I'm at work and don't have access to the router, I can't use Gitso to give support.

  * **Q:** (Ubuntu) When I try to install Gitso, it says "Dependency is not satisfiable: x11vnc". What's up?
  * **A:** This is because that program isn't enabled for install by default, please follow these steps to enable it.
    1. Enable universe repository by going to the following menu:
> > > System > Administration > Software Sources > check all > Close > Reload
    1. Now you should be able to install Gitso by double clicking gitso\_0.6\_all.deb and then clicking "Install Package".

  * **Q:** (Windows  - Get help) I'm not able to get help, I know I have IP's and the support guys says his network is set-up correctly.
  * **A:** Selecting "Unblock" when prompted by Windows Firewall or disable the firewall on that port.

  * **Q:** Why is there no temporary shared secret needed to make sure the connection is legitimate and not accidental or manipulative?
  * **A:** Because Gitso is based on reverse VNC, you have to connect to someone to share your screen, not the other-way around; as such it reduces the need for a password. Specifically, the server that is running, allows you to connect to other peoples' screens, not to share your screen (which is traditionally used).


## Advanced ##
There are a number of command line switches that Gitso supports.
  * **--dev** This should be used when calling gitso from the source. This enables the code to look in the appropriate place for various assets.
  * **--listen** Gitso will start and automatically listen for connections (AKA give support)..
  * **--connect IP** Gitso will start and automatically try to connect to the IP address.
  * **--list list\_file** Gitso will look to this external list, can be local or via HTTP for the hosts lists. Ex: You could add a list to your web server so every time the user connected with this option, they would get an up-to-date support list from your server.
    * **list\_file** Should be something like http://www.myserver.com/path/to/support_ips.txt
    * **support\_ips.txt** Should be a comma separated list of IP's. These will then show up in the menu of support IP addresses in Gitso.
  * **--low-colors** Use 8bit colors (for slow connections). Linux only.
  * **--version** Show the current release of Gitso.
  * **--help** Show these options.