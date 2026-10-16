FAVICON_HREF = "data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2064%2064'%3E%3Crect%20width='64'%20height='64'%20rx='12'%20fill='%23ff5a2c'/%3E%3Cpath%20d='M46%2032H19M31%2019L18%2032L31%2045'%20fill='none'%20stroke='%230a0c0f'%20stroke-width='6'%20stroke-linecap='round'%20stroke-linejoin='round'/%3E%3C/svg%3E"

# The experimental-status strip shown under the header of every page.
# One text, three emitters (landing, portal, docs renderer); the markup is
# `.fl-banner` in speculum.css.
EXPERIMENTAL_LEAD = "Experimental through version 1."
EXPERIMENTAL_BODY = (
    "Version 0 was alpha. This is the first language release: the interface "
    "is relatively stable, not frozen. Nothing is promised stable until "
    "version 2."
)


def experimental_banner_html():
    return (
        '<div class="fl-banner" role="status">\n'
        f"  <p><strong>{EXPERIMENTAL_LEAD}</strong>\n"
        f"  {EXPERIMENTAL_BODY}</p>\n"
        "</div>\n"
    )
