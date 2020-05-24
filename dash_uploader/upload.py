import uuid

import dash_html_components as html

from dash_uploader._build.Upload_ReactComponent import Upload_ReactComponent

DEFAULT_STYLE = {
    'width': '100%',
    # min-height and line-height should be the same to make
    # the centering work.
    'minHeight': '100px',
    'lineHeight': '100px',
    'textAlign': 'center',
    'borderWidth': '1px',
    'borderStyle': 'dashed',
    'borderRadius': '7px',
}


def combine(overiding_dict, base_dict):
    if overiding_dict is None:
        return dict(base_dict)
    return {**base_dict, **overiding_dict}


# Implemented as function, but still uppercase.
# This is because subclassing the Dash-auto-generated
# "Upload from Upload.py" will give some errors
def Upload(
    id='dash-uploader',
    text='Drag and Drop Here to upload!',
    text_completed='Uploaded: ',
    cancel_button=True,
    pause_button=False,
    filetypes=None,
    max_file_size=1024,
    default_style=None,
    upload_id=None,
):
    """
    Parameters
    ----------
    text: str
        The text to show in the upload "Drag
        and Drop" area. Optional.
    text_completed: str
        The text to show in the upload area 
        after upload has completed succesfully before
        the name of the uploaded file. For example, if user
        uploaded "data.zip" and `text_completed` is 
        "Ready! ", then user would see text "Ready! 
        data.zip".
    cancel_button: bool
        If True, shows a cancel button.
    pause_button: bool
        If True, shows a pause button.
    filetypes: list of str or None
        The filetypes that can be uploaded. 
        For example ['zip', 'rar'].
        Note that this just checks the extension of the 
        filename, and user might still upload any kind 
        of file (by renaming)!
        By default, all filetypes are accepted.
    max_file_size: numeric
        The maximum file size in Megabytes. Optional.
    default_style: None or dict
        Inline CSS styling for the main div element. 
        If None, use the default style of the component.
        If dict, will use the union on the given dict
        and the default style. (you may override
        part of the style by giving a dictionary)
        More styling options through the CSS classes.
    upload_id: None or str
        The upload id, created with uuid.uuid1() or uuid.uuid4(), 
        for example. If none, creates random session id with
        uuid.uuid1().

    Returns
    -------
    Upload: dash component
        Initiated Dash component for app.layout.
    """

    # Handle styling
    default_style = combine(default_style, DEFAULT_STYLE)
    upload_style = combine({'lineHeight': '0px'}, default_style)

    if upload_id is None:
        upload_id = uuid.uuid1()

    arguments = dict(
        id=id,
        # Have not tested if using many files
        # is reliable -> Do not allow
        maxFiles=1,
        maxFileSize=max_file_size * 1024 * 1024,
        textLabel=text,
        service='/API/resumable',
        startButton=False,
        # Not tested so default to one.
        simultaneousUploads=1,
        completedMessage=text_completed,
        cancelButton=cancel_button,
        pauseButton=pause_button,
        defaultStyle=default_style,
        uploadingStyle=upload_style,
        completeStyle=default_style,
        upload_id=str(upload_id),
    )

    if filetypes:
        arguments['filetypes'] = filetypes

    return Upload_ReactComponent(**arguments)
