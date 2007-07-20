
%define plugin	vompserver
%define name	vdr-plugin-%plugin
%define version	0.2.6
%define rel	1

Summary:	VDR plugin: VDR on MVP plugin
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.loggytronic.com/vomp.php
Source:		http://www.loggytronic.com/dl/vdr-%plugin-%version.tgz
# e-tobi
Patch0:		vompserver-vdr-1.5.0.dpatch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
Requires:	vdr-abi = %vdr_abi

%description
VOMP brings Video Disk Recorder (VDR) functionality to other
devices. There is a plugin for VDR and client software for the
Hauppauge MVP and now also Windows. The clients talk to the server
over a network. The original idea was to make a clean set-top-box
out of the MVP with an easy user interface much like a normal
digital TV consumer set-top-box. 

%prep
%setup -q -n %plugin-%version
%patch0 -p1

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY *.sample
