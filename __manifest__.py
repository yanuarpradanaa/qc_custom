{
    'name': "Quality Control PP Custom",
    'summary': """
     Quality Control Custom
    """,
    'description': """
    Quality Control Custom PP\n

     Update v1.2 (07/02/2020):\n
      - [NEW] Create Multiple Picking from One QC Sheet\n
      - [ADD] One2many Line for Multiple Picking\n\n
     Update v1.1:\n
      - [CHANGE] Qty -> Qty Kirim (FormView & TreeView)\n
      - [ADD] Qty Sample (FormView & TreeView)\n\n
     v1.0:\n
     FormView:\n
      - [ADD] field Product Dropdown\n
      - [ADD] field SO Reference Dropdown\n
      - [ADD] field Description\n
     TreeView:\n
      - [CHANGE] Production -> Description\n
      - [CHANGE] Quantity -> Qty (pcs)\n
      - [ADD] field Date\n
      - [ADD] field Sales Order\n
     \n
     Other Custom:\n
     - Reference editable ketika state Success\n
    """,
    'author': "Satusoft",
    'website': "https://satusoft.com/",
    'category': 'Prima Print Modul',
    'version': '1.2',
    'depends': [
        'base',
        'quality_control',
        'quality_control_stock',
        'quality_control_mrp',
    ],
    'data': [
        'views/views.xml',
        'views/action_button.xml',
    ],
}