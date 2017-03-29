import React from 'react'
import classnames from 'classnames'
import AnnotationDetail from './AnnotationDetail'
import styles from './AnnotationControls.css'

const AnnotationControls = (props) => {

    let annotations = [];
    let variantsHeading = null;
    let nothingSelected = null;
    if (props.annotationsData) {
        props.annotationsData.map((annotationData) => {
            let isActive = false;
            if (annotationData.id == props.activeAnnotation.id) {
                isActive = true;
            }
            let annotationDetail = <AnnotationDetail
                annotationData={annotationData}
                key={annotationData.id}
                isActive={isActive}
                onClickHandler={() => {
                    props.didSelectAnnotation(annotationData.id);
                }}/>;
            annotations.push(annotationDetail);
        }, this);
        variantsHeading = <h3>Variants</h3>;
    } else {
        nothingSelected = <div className={styles.nothingSelected}>Nothing Selected</div>;
    }

    return (
        <div className={styles.annotationControls} >
            {nothingSelected}
            {variantsHeading}
            {annotations}
        </div>
    )
};

export default AnnotationControls;
