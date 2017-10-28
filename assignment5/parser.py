import re


source_text = """%Lorem% ipsum *dolor sit amet*, consectetur *adipiscing elit. Nullam tempor* nunc at justo tincidunt congue. %Aliquam hendrerit mollis pretium! Praesent id% mi est. [Praesent,](www.praesent.com) sed orci aliquet, dapibus elit sed, maximus dolor. Donec ut viverra velit, in sollicitudin nisl. Aliquam nec orci sit amet sem congue condimentum. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.

>>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse a nulla *eget eros euismod volutpat. Suspendisse* id luctus lorem. Vivamus non erat bibendum lacus sodales convallis scelerisque ac diam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus eget quam eros. Nulla lectus turpis, porttitor sed laoreet id, varius eget dolor. Proin non sapien et risus dictum suscipit quis id leo. Aenean at mauris vel eros gravida gravida. Sed feugiat %molestie \*libero vel\%\% pulvinar? Sed% a accumsan risus, at vehicula felis. Nullam eget est blandit eros consectetur facilisis. Etiam ligula augue, fringilla ac nibh sit amet, posuere dignissim libero. Nunc accumsan odio leo, et mollis turpis aliquam eu. Proin sed maximus erat. Maecenas diam velit, tristique et posuere ut, placerat sit amet diam.

Curabitur finibus, turpis viverra rutrum consequat, ligula tortor consectetur ex, eu malesuada lacus ipsum in \%% urna. \% Fusce% in *sapien %mau\*ris.% Duis purus dui*, viverra in tellus eu, imperdiet fringilla [felis. Curabitur rhoncus tincidunt varius. Cras](inf3331.no) gravida metus ut [wp:vestibulum] vestibulum. \*Integer cursus* ex\* in rutrum volutpat*. Nunc scelerisque gravida risus sed ullamcorper. Proin [lorem,](https://www.malesuada.com) massa <https://www.mn.uio.no/astro/english/services/it/help/basic-services/latex/uiologo.gif>(w=100,h=40) quam in, scelerisque elementum arcu. Nunc scelerisque sem ac lectus porttitor, sed molestie odio *bibendum.*
"""

source_text_test = """%Lorem% ipsum *dolor sit amet*, consectetur *adipiscing elit. Nullam tempor* nunc at justo tincidunt congue. %Aliquam hendrerit mollis pretium! Praesent id% mi est. [Praesent,](www.praesent.com) sed orci aliquet, dapibus elit sed, maximus dolor. Donec ut viverra velit, in sollicitudin nisl. Aliquam nec orci sit amet sem congue condimentum. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.

>>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse a nulla *eget eros euismod volutpat. Suspendisse* id luctus lorem. Vivamus non erat bibendum lacus sodales convallis scelerisque ac diam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus eget quam eros. Nulla lectus turpis, porttitor sed laoreet id, varius eget dolor. Proin non sapien et risus dictum suscipit quis id leo. Aenean at mauris vel eros gravida gravida. Sed feugiat %molestie \*libero vel\%\% pulvinar? Sed% a accumsan risus, at vehicula felis. Nullam eget est blandit eros consectetur facilisis. Etiam ligula augue, fringilla ac nibh sit amet, posuere dignissim libero. Nunc accumsan odio leo, et mollis turpis aliquam eu. Proin sed maximus erat. Maecenas diam velit, tristique et posuere ut, placerat sit amet diam.

Curabitur finibus, turpis viverra rutrum consequat, ligula tortor consectetur ex, eu malesuada lacus ipsum in \%% urna. \% Fusce% in *sapien %mau\*ris.% Duis purus dui*, viverra in tellus eu, imperdiet fringilla [felis. Curabitur rhoncus tincidunt varius. Cras](inf3331.no) gravida metus ut [wp:vestibulum] vestibulum. \*Integer cursus* ex\* in rutrum volutpat*. Nunc scelerisque gravida risus sed ullamcorper. Proin [lorem,](https://www.malesuada.com) massa <https://www.mn.uio.no/astro/english/services/it/help/basic-services/latex/uiologo.gif>(w=100,h=40) quam in, scelerisque elementum arcu. Nunc scelerisque sem ac lectus porttitor, sed molestie odio *bibendum.*
"""


bold_tag = r"(?:(?<!\\)%)"
bold_in = bold_tag + r"((?:\\%|[^%])+)" + bold_tag
bold_out = r"<b>\1</b>"

italic_tag = r"(?:(?<!\\)\*)"
italic_in = italic_tag + r"((?:\\\*|[^\*])+)" + italic_tag
italic_out = r"<i>\1</i>"

link = r"\[([^\[\]]+)\]\((.+)\)"

escaped_tags_in = r"\\([%\*])"

# search_results = re.findall(bold, source_text_test)
# print(search_results)

# bolding
substituted_text = re.sub(bold_in, bold_out, source_text)
# italizing
substituted_text = re.sub(italic_in, italic_out, substituted_text)
# escaped characters
substituted_text = re.sub(escaped_tags_in, r"\1", substituted_text)

# print(substituted_text)

filename = "hui"
with open('out.html', 'w') as f:
    print(substituted_text, file=f)
