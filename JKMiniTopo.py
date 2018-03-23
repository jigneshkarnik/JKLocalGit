#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call
import sys

def myNetwork():

    net = Mininet( topo=None,build=False,ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )

    c0=net.addController(name='c0',controller=Controller,protocol='tcp', port=6633)

    c1=net.addController(name='c1',controller=Controller,protocol='tcp', port=6634)

    c2=net.addController(name='c2',controller=Controller,protocol='tcp', port=6635)

    info( '*** Add switches\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)    
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch)
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch)
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch)
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch)
    s8 = net.addSwitch('s8', cls=OVSKernelSwitch)
    
    
    

    info( '*** Add hosts\n')
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='10.0.0.5', defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='10.0.0.6', defaultRoute=None)
    h7 = net.addHost('h7', cls=Host, ip='10.0.0.7', defaultRoute=None)
    h8 = net.addHost('h8', cls=Host, ip='10.0.0.8', defaultRoute=None)
    h9 = net.addHost('h9', cls=Host, ip='10.0.0.9', defaultRoute=None)
    h10 = net.addHost('h10', cls=Host, ip='10.0.0.10', defaultRoute=None)
    
    info( '*** Add links\n')
    net.addLink(s2, h4)
    net.addLink(s3, h5)
    net.addLink(s3, h6)
    net.addLink(s1, h1)
    net.addLink(s1, h2)
    net.addLink(s2, h3)
    net.addLink(s4, h7)
    net.addLink(s4, h8)
    net.addLink(s5, h9)
#    net.addLink(s5, h10)
    net.addLink(s6, s1)
    net.addLink(s6, s2)
    net.addLink(s8, s3)
    net.addLink(s8, s4)
    net.addLink(s8, s5)
    net.addLink(s7, s6)
    net.addLink(s7, s8)
    
    net.build()
    
    info( '*** Starting controllers\n')
    
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    
    
    
    net.get('s1').start([c0])
    net.get('s2').start([c0])
    
    net.get('s6').start([c1])
    net.get('s7').start([c1])
    net.get('s8').start([c1])
    
    net.get('s3').start([c2])
    net.get('s4').start([c2])
    net.get('s5').start([c2])
   
    return net
