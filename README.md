<p>
<a href="https://flathub.org/apps/details/se.sjoerd.Graphs"><img height="62" alt="Download on Flathub" src="https://flathub.org/assets/badges/flathub-badge-en.svg"/></a>&nbsp;&nbsp;
<a href="https://snapcraft.io/graphs"><img height="60" alt="Get it from the Snap Store" src="https://snapcraft.io/static/images/badges/en/snap-store-black.svg"/></a>
</p>

# Graphs

![image](https://raw.githubusercontent.com/Sjoerd1993/Graphs/main/data/screenshots/sin_cos.png)


Graphs is a simple, yet powerful tool that allows you to plot and manipulate your data with ease. You can import data from two-column files or generate it via an equation. All data can be manipulated using a variety of operations.
Graphs lets you customize the style of plotted data. You can add and edit stylesheets in detail.
Graphs is an excellent fit for both plotting and data manipulation. The plots created with Graphs can be saved in a variety of formats suitable for sharing and presenting to a wide audience, such as in a scientific publication or presentations. It is also possible to save the plots as vector images, which can be easily edited in programs like Inkscape for further customization and refinement. Graphs is written with the GNOME environment in mind, but should be suitable for any other desktop environment as well.

The operations include:
  - Shifting data
  - Normalizing Data
  - Smoothening data
  - Centering Data
  - Cutting Data
  - Combining Data
  - Translating data
  - Derivative and indefinite integral
  - Fourier Transformations
  - Custom transformations using anything that is compatible with the numpy module
 
For feedback or general issues, please file an issue [at the Github issue tracker](https://github.com/SjoerdB93/Graphs/issues).

## How to contribute
### Translations


Graphs is translated using Weblate.
If you wish to contribute to the translation of Graphs, in other languages please check out the project page on [Weblate](https://hosted.weblate.org/engage/graphs/).
We are incredibly grateful to anyone helping to make Graphs available in different languages!

<a href="https://hosted.weblate.org/engage/graphs/">
<img src="https://hosted.weblate.org/widget/graphs/multi-auto.svg" alt="Translation status" />
</a>

### Code 

If you wish to contribute to the code of Graphs, feel free to submit a [Pull request](https://github.com/Sjoerd1993/Graphs/pulls). 
We are always happy for contributions, and new code is generally reviewed within a few days time.

### Feedback and bug reports

If you found an issue or have general feedback, please file an issue at the [issue tracker](https://github.com/Sjoerd1993/Graphs/issues).


## How to build
This project is developed in [GNOME Builder](https://developer.gnome.org/documentation/introduction/builder.html). After cloning and opening the project, you can press run to verify you have all correct dependencies installed.
You might need to install meson, if it is not already availabe on your system.
When the project successfully ran, you can create a flatpak-bundle on the buildchain menu, which you then can install on your system.

If you want to try the latest development, we urge you to try the flathub beta branch instead of building yourself.

### Build without flatpak
This project targets the GNOME Platform on flathub. Any other platform is currently **not supported**.

If you want to build without flatpak anyway these instructions might help:

build-time dependencies: `meson, blueprint-compiler, gettext`

runtime dependencies: `matplotlib, python3-matplotlib-gtk4, scipy, numpy`

The actual package names might vary depending on your distribution.

building:
```
git clone https://github.com/Sjoerd1993/Graphs.git
cd Graphs
meson setup build
ninja -C build
ninja -C build/ install
```
Uninstall could then be done with the following:
```
ninja -C build/ uninstall
```

Please note, that this install might have issues, that the flatpak version does not.

## Code of Conduct
This project follows the [GNOME Code of Conduct](https://wiki.gnome.org/Foundation/CodeOfConduct).
